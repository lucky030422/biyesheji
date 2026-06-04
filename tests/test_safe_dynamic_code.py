import builtins
import os
import unittest
from unittest.mock import patch

from django.db.models import Q
from django.test import RequestFactory


class FakeQuerySet(list):
    def __init__(self, rows):
        super().__init__(rows)
        self.filters = []
        self.ordering = []

    def filter(self, *args, **kwargs):
        self.filters.append((args, kwargs))
        return self

    def order_by(self, *fields):
        self.ordering.extend(fields)
        return self

    def all(self):
        return self

    def values(self):
        return list(self)


class FakeManager:
    def __init__(self):
        self.queryset = FakeQuerySet([{"id": 1, "name": "alpha", "score": 5}])

    def filter(self, **kwargs):
        return self.queryset.filter(**kwargs)


class FakeModel:
    __tablename__ = "fake"
    objects = FakeManager()

    class _Meta:
        fields = []

    _meta = _Meta()


class ModelHarness:
    def to_list(self, datas, *args):
        if hasattr(datas, "values"):
            return list(datas.values())
        return list(datas)


class SafeDynamicCodeTests(unittest.TestCase):
    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj2.settings")

        import django

        django.setup()

    def test_schema_upload_does_not_use_eval_to_resolve_filename(self):
        from main.schema_v import schemaName_upload

        request = RequestFactory().get("/upload/example.png")

        with patch.object(builtins, "eval", side_effect=AssertionError("eval called")):
            with patch("main.schema_v.check_suffix") as check_suffix:
                schemaName_upload(request, "example.png")

        self.assertEqual(check_suffix.call_args.args[0], "example.png")
        self.assertTrue(check_suffix.call_args.args[1].endswith("templates/upload/example.png"))

    def test_dj2_static_views_do_not_use_eval_to_resolve_filename(self):
        from dj2.views import admin_lib2

        request = RequestFactory().get("/admin/lib/layui/layui.js")

        with patch.object(builtins, "eval", side_effect=AssertionError("eval called")):
            with patch("dj2.views.check_suffix") as check_suffix:
                admin_lib2(request, "layui", "layui.js")

        self.assertEqual(check_suffix.call_args.args[0], "layui.js")
        self.assertTrue(
            os.path.normpath(check_suffix.call_args.args[1]).endswith(
                os.path.normpath("templates/front/admin/lib/layui/layui.js")
            )
        )

    def test_page_query_building_does_not_use_eval(self):
        from main.model import BaseModel

        params = {"name": "%alp%", "scorestart": "1", "scoreend": "10", "sort": "id", "order": "desc", "page": "1", "limit": "10"}

        with patch.object(builtins, "eval", side_effect=AssertionError("eval called")):
            with patch("django.apps.apps.get_model", return_value=FakeModel):
                data, page, pages, total, limit = BaseModel._BaseModel__Page(
                    ModelHarness(), FakeModel, params, {}, Q()
                )

        self.assertEqual(data, [{"id": 1, "name": "alpha", "score": 5}])
        self.assertEqual(page, "1")
        self.assertEqual(total, 1)
        self.assertEqual(limit, "10")
        self.assertIn("-id", FakeModel.objects.queryset.ordering)

    def test_between_query_building_does_not_use_eval(self):
        from main.model import BaseModel

        params = {"remindstart": "1", "remindend": "10", "type": "1"}

        with patch.object(builtins, "eval", side_effect=AssertionError("eval called")):
            data = BaseModel._BaseModel__GetBetweenParams(BaseModel, FakeModel, "score", params)

        self.assertEqual(data, [{"id": 1, "name": "alpha", "score": 5}])


if __name__ == "__main__":
    unittest.main()
