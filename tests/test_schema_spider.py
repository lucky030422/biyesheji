import os
import unittest
from unittest.mock import patch

from django.test import RequestFactory


class SchemaSpiderTests(unittest.TestCase):
    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj2.settings")

        import django

        django.setup()

    def test_spider_rejects_invalid_table_name_without_running_command(self):
        from main.schema_v import schemaName_spider

        request = RequestFactory().get("/spider/bad;name")

        with patch("main.schema_v.os.system") as system:
            response = schemaName_spider(request, "bad;name")

        self.assertEqual(response.status_code, 400)
        system.assert_not_called()


if __name__ == "__main__":
    unittest.main()
