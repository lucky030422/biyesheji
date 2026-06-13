import os
import time
from pathlib import Path

import pytest
import requests


class ApiTestCase:
    BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8080/djangoq0l722c8").rstrip("/")
    ADMIN_USER = os.getenv("API_ADMIN_USER", "admin")
    ADMIN_PASSWORD = os.getenv("API_ADMIN_PASSWORD", "admin")
    FRONT_USER = os.getenv("API_FRONT_USER", "422")
    FRONT_PASSWORD = os.getenv("API_FRONT_PASSWORD", "123456")
    TIMEOUT = float(os.getenv("API_TEST_TIMEOUT", "10"))
    UPLOAD_DIR = Path(__file__).resolve().parents[1] / "templates" / "upload"

    @classmethod
    def setup_class(cls):
        cls.http = requests.Session()
        cls.admin_token = None
        cls.front_token = None
        cls.front_profile = None
        try:
            response = cls.raw_request("GET", "/chongwufuwu/list", params={"page": 1, "limit": 1})
            if response.status_code >= 500:
                response.raise_for_status()
        except requests.RequestException as exc:
            pytest.skip(f"API service is unavailable: {exc}")

    @classmethod
    def url(cls, path):
        return f"{cls.BASE_URL}/{path.lstrip('/')}"

    @classmethod
    def raw_request(cls, method, path, **kwargs):
        kwargs.setdefault("timeout", cls.TIMEOUT)
        return cls.http.request(method, cls.url(path), **kwargs)

    @classmethod
    def json_request(cls, method, path, **kwargs):
        response = cls.raw_request(method, path, **kwargs)
        body = cls.parse_json(response)
        return response, body

    @staticmethod
    def parse_json(response):
        try:
            return response.json()
        except ValueError:
            return None

    def get_json(self, path, token=None, **kwargs):
        headers = kwargs.pop("headers", {})
        if token:
            headers["token"] = token
        return self.json_request("GET", path, headers=headers, **kwargs)

    def post_json(self, path, payload=None, token=None, **kwargs):
        headers = kwargs.pop("headers", {})
        if token:
            headers["token"] = token
        return self.json_request("POST", path, json={} if payload is None else payload, headers=headers, **kwargs)

    def post_form(self, path, data=None, token=None, files=None, **kwargs):
        headers = kwargs.pop("headers", {})
        if token:
            headers["token"] = token
        return self.json_request("POST", path, data=data or {}, files=files, headers=headers, **kwargs)

    def assert_http_ok(self, response):
        self.assertLess(response.status_code, 500, response.text[:300])

    def assert_json(self, response, body):
        self.assertIsInstance(body, dict, f"Expected JSON object, got {response.status_code}: {response.text[:300]}")

    def assert_api_ok(self, response, body):
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.assertEqual(body.get("code"), 0, body)

    def assert_api_fail(self, response, body):
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.assertNotEqual(body.get("code"), 0, body)

    def assert_api_fail_cleanup(self, table, response, body):
        try:
            self.assert_api_fail(response, body)
        finally:
            if isinstance(body, dict) and body.get("code") == 0 and isinstance(body.get("data"), int):
                self.cleanup_record(table, body.get("data"))

    def assert_page_payload(self, response, body):
        self.assert_api_ok(response, body)
        data = body.get("data")
        self.assertIsInstance(data, dict, body)
        self.assertIn("list", data)
        self.assertIsInstance(data["list"], list)
        self.assertIn("total", data)

    def assert_empty_or_error(self, response, body):
        self.assert_http_ok(response)
        if body is None:
            return
        self.assert_json(response, body)
        if body.get("code") == 0:
            self.assertIn(body.get("data"), ({}, None, [], ""))

    def login_admin(self):
        if not self.__class__.admin_token:
            response, body = self.post_json(
                "/users/login",
                {"username": self.ADMIN_USER, "password": self.ADMIN_PASSWORD},
            )
            self.assert_api_ok(response, body)
            self.__class__.admin_token = body.get("token")
            self.assertTrue(self.__class__.admin_token)
        return self.__class__.admin_token

    def login_front(self):
        if not self.__class__.front_token:
            response, body = self.post_json(
                "/yonghu/login",
                {"username": self.FRONT_USER, "password": self.FRONT_PASSWORD},
            )
            self.assert_api_ok(response, body)
            self.__class__.front_token = body.get("token")
            self.assertTrue(self.__class__.front_token)
        return self.__class__.front_token

    def front_user(self):
        if not self.__class__.front_profile:
            token = self.login_front()
            response, body = self.get_json("/yonghu/session", token=token)
            self.assert_api_ok(response, body)
            self.__class__.front_profile = body.get("data") or {}
        return self.__class__.front_profile

    def first_record(self, table, token=None):
        response, body = self.get_json(f"/{table}/list", token=token, params={"page": 1, "limit": 1})
        self.assert_page_payload(response, body)
        rows = body["data"]["list"]
        if not rows:
            self.skipTest(f"{table} has no data")
        return rows[0]

    def first_id(self, table, token=None):
        return self.first_record(table, token=token)["id"]

    def cleanup_record(self, table, record_id):
        if record_id:
            self.post_json(f"/{table}/delete", [record_id], token=self.login_admin())

    def unique(self, prefix):
        return f"{prefix}_{int(time.time() * 1000)}"

    def assertEqual(self, first, second, msg=None):
        assert first == second, msg or f"{first!r} != {second!r}"

    def assertNotEqual(self, first, second, msg=None):
        assert first != second, msg or f"{first!r} == {second!r}"

    def assertTrue(self, expr, msg=None):
        assert expr, msg or f"{expr!r} is not truthy"

    def assertFalse(self, expr, msg=None):
        assert not expr, msg or f"{expr!r} is not falsy"

    def assertIn(self, member, container, msg=None):
        assert member in container, msg or f"{member!r} not found in {container!r}"

    def assertNotIn(self, member, container, msg=None):
        assert member not in container, msg or f"{member!r} unexpectedly found in {container!r}"

    def assertIsInstance(self, obj, cls, msg=None):
        assert isinstance(obj, cls), msg or f"{obj!r} is not an instance of {cls!r}"

    def assertLess(self, first, second, msg=None):
        assert first < second, msg or f"{first!r} is not less than {second!r}"

    def assertLessEqual(self, first, second, msg=None):
        assert first <= second, msg or f"{first!r} is not less than or equal to {second!r}"

    def assertGreaterEqual(self, first, second, msg=None):
        assert first >= second, msg or f"{first!r} is not greater than or equal to {second!r}"

    def order_common(self, prefix):
        user = self.front_user()
        return {
            "dingdanbianhao": self.unique(prefix),
            "zhanghao": user.get("zhanghao", self.FRONT_USER),
            "xingming": user.get("xingming", "api-test"),
            "shoujihaoma": user.get("shoujihaoma", "13800000000"),
            "xiadanshijian": "2026-06-13",
        }

    def service_order_payload(self, **overrides):
        service = self.first_record("chongwufuwu")
        payload = {
            **self.order_common("FW"),
            "fuwumingcheng": service.get("fuwumingcheng", "api-service"),
            "fuwufengmian": service.get("fuwufengmian", ""),
            "fuwuleixing": service.get("fuwuleixing", "api-type"),
            "jifen": service.get("jifen", 1),
            "fuwushizhang": service.get("fuwushizhang", "1h"),
            "chongwuxingming": "api-pet",
            "pinzhong": "api-kind",
            "yuyueriqi": "2026-06-14",
            "beizhu": "api-test",
        }
        payload.update(overrides)
        return payload

    def foster_order_payload(self, **overrides):
        service = self.first_record("jiyangfuwu")
        payload = {
            **self.order_common("JY"),
            "fuwumingcheng": service.get("fuwumingcheng", "api-foster"),
            "fuwufengmian": service.get("fuwufengmian", ""),
            "fuwuleixing": service.get("fuwuleixing", "api-type"),
            "jifen": service.get("jifen", 1),
            "jiyangriqi": "2026-06-14",
            "chongwuxingming": "api-pet",
            "pinzhong": "api-kind",
            "beizhu": "api-test",
        }
        payload.update(overrides)
        return payload

    def goods_order_payload(self, **overrides):
        goods = self.first_record("chongwuyongpin")
        payload = {
            **self.order_common("SP"),
            "shangpinmingcheng": goods.get("shangpinmingcheng", "api-goods"),
            "shangpinfengmian": goods.get("shangpinfengmian", ""),
            "shangpinleixing": goods.get("shangpinleixing", "api-type"),
            "guige": goods.get("guige", "api-spec"),
            "pinpai": goods.get("pinpai", "api-brand"),
            "chandi": goods.get("chandi", "api-origin"),
            "jiage": goods.get("jiage", 1),
            "kucun": 1,
            "jifen": goods.get("jiage", 1),
            "shouhuodizhi": self.front_user().get("shouhuodizhi", "api-address"),
        }
        payload.update(overrides)
        return payload

    def apply_payload(self, **overrides):
        pet = self.first_record("lingyangchongwu")
        user = self.front_user()
        payload = {
            "shenqingbianhao": self.unique("LY"),
            "chongwunicheng": pet.get("chongwunicheng", "api-pet"),
            "chongwupinzhong": pet.get("chongwupinzhong", "api-kind"),
            "chongwutupian": pet.get("chongwutupian", ""),
            "xingbie": pet.get("xingbie", "unknown"),
            "xinggetedian": pet.get("xinggetedian", "api-feature"),
            "shenqingriqi": "2026-06-13",
            "lingyangshuoming": "api apply",
            "zhanghao": user.get("zhanghao", self.FRONT_USER),
            "xingming": user.get("xingming", "api-test"),
            "shoujihaoma": user.get("shoujihaoma", "13800000000"),
        }
        payload.update(overrides)
        return payload

    def service_payload(self, **overrides):
        payload = {
            "fuwumingcheng": self.unique("api_service"),
            "fuwufengmian": "upload/api.jpg",
            "fuwuleixing": "api-type",
            "fuwufanwei": "api-range",
            "chongwuleixing": "api-pet",
            "jifen": 10,
            "fuwushizhang": "1h",
            "fuwujieshao": "api intro",
        }
        payload.update(overrides)
        return payload


class TestAuthApi(ApiTestCase):
    def test_API_AUTH_001_user_login_success(self):
        response, body = self.post_json("/yonghu/login", {"username": self.FRONT_USER, "password": self.FRONT_PASSWORD})
        self.assert_api_ok(response, body)
        self.assertTrue(body.get("token"))
        self.assertIn("id", body)

    def test_API_AUTH_002_user_login_wrong_password(self):
        response, body = self.post_json("/yonghu/login", {"username": self.FRONT_USER, "password": "wrongpwd"})
        self.assert_api_fail(response, body)
        self.assertFalse(body.get("token"))

    def test_API_AUTH_003_user_login_unknown_account(self):
        response, body = self.post_json("/yonghu/login", {"username": "not_exists", "password": "123456"})
        self.assert_api_fail(response, body)

    def test_API_AUTH_004_user_login_empty_account(self):
        response, body = self.post_json("/yonghu/login", {"username": "", "password": "123456"})
        self.assert_api_fail(response, body)

    def test_API_AUTH_005_user_login_empty_password(self):
        response, body = self.post_json("/yonghu/login", {"username": self.FRONT_USER, "password": ""})
        self.assert_api_fail(response, body)

    def test_API_AUTH_006_user_login_long_account(self):
        response, body = self.post_json("/yonghu/login", {"username": "u" * 300, "password": "123456"})
        self.assert_api_fail(response, body)

    def test_API_ADMIN_LOGIN_001_admin_login_success(self):
        response, body = self.post_json("/users/login", {"username": self.ADMIN_USER, "password": self.ADMIN_PASSWORD})
        self.assert_api_ok(response, body)
        self.assertTrue(body.get("token"))

    def test_API_ADMIN_LOGIN_002_admin_login_wrong_password(self):
        response, body = self.post_json("/users/login", {"username": self.ADMIN_USER, "password": "wrongpwd"})
        self.assert_api_fail(response, body)

    def test_API_ADMIN_LOGIN_003_admin_login_empty_account(self):
        response, body = self.post_json("/users/login", {"username": "", "password": self.ADMIN_PASSWORD})
        self.assert_api_fail(response, body)

    def test_API_ADMIN_LOGIN_004_admin_login_wrong_content_type(self):
        response = self.raw_request(
            "POST",
            "/users/login",
            data='{"username":"admin","password":"admin"}',
            headers={"Content-Type": "text/plain"},
        )
        body = self.parse_json(response)
        self.assert_http_ok(response)
        self.assertTrue(body is None or body.get("code") != 0)

    def test_API_SESSION_001_user_session_valid_token(self):
        response, body = self.get_json("/yonghu/session", token=self.login_front())
        self.assert_api_ok(response, body)
        self.assertEqual(str(body.get("data", {}).get("zhanghao")), str(self.FRONT_USER))

    def test_API_SESSION_002_user_session_without_token(self):
        response, body = self.get_json("/yonghu/session")
        self.assert_api_fail(response, body)

    def test_API_SESSION_003_user_session_fake_token(self):
        response, body = self.get_json("/yonghu/session", token="fake-token")
        self.assert_api_fail(response, body)

    def test_API_SESSION_004_user_session_sensitive_fields(self):
        response, body = self.get_json("/yonghu/session", token=self.login_front())
        self.assert_api_ok(response, body)
        self.assertNotIn("mima", body.get("data", {}), "Session response exposes password field mima")


class TestPublicQueryApi(ApiTestCase):
    def test_API_SERVICE_LIST_001_service_list_first_page(self):
        response, body = self.get_json("/chongwufuwu/list", params={"page": 1, "limit": 5})
        self.assert_page_payload(response, body)
        self.assertLessEqual(len(body["data"]["list"]), 5)

    def test_API_SERVICE_LIST_002_service_list_search_name(self):
        response, body = self.get_json("/chongwufuwu/list", params={"page": 1, "limit": 5, "fuwumingcheng": "cat"})
        self.assert_page_payload(response, body)

    def test_API_SERVICE_LIST_003_service_list_no_result(self):
        response, body = self.get_json("/chongwufuwu/list", params={"page": 1, "limit": 5, "fuwumingcheng": "not-exists-xyz"})
        self.assert_page_payload(response, body)
        self.assertTrue(body["data"]["total"] == 0 or body["data"]["list"] == [])

    def test_API_SERVICE_LIST_004_service_list_large_page(self):
        response, body = self.get_json("/chongwufuwu/list", params={"page": 999999, "limit": 5})
        self.assert_page_payload(response, body)

    def test_API_SERVICE_LIST_005_service_list_invalid_page(self):
        response, body = self.get_json("/chongwufuwu/list", params={"page": "abc", "limit": -1})
        self.assert_http_ok(response)
        self.assert_json(response, body)

    def test_API_SERVICE_LIST_006_service_list_sql_injection_chars(self):
        response, body = self.get_json("/chongwufuwu/list", params={"page": 1, "limit": 5, "fuwumingcheng": "' OR 1=1 --"})
        self.assert_page_payload(response, body)
        self.assertLessEqual(len(body["data"]["list"]), 5)

    def test_API_SERVICE_DETAIL_001_service_detail_valid_id(self):
        record_id = self.first_id("chongwufuwu")
        response, body = self.get_json(f"/chongwufuwu/detail/{record_id}")
        self.assert_api_ok(response, body)
        self.assertEqual(int(body["data"]["id"]), int(record_id))

    def test_API_SERVICE_DETAIL_002_service_detail_not_found(self):
        response, body = self.get_json("/chongwufuwu/detail/999999")
        self.assert_empty_or_error(response, body)

    def test_API_SERVICE_DETAIL_003_service_detail_invalid_id(self):
        response, body = self.get_json("/chongwufuwu/detail/abc")
        self.assert_http_ok(response)
        if body is not None:
            self.assertNotEqual(body.get("code"), 0)

    def test_API_SERVICE_DETAIL_004_service_info_valid_id(self):
        record_id = self.first_id("chongwufuwu")
        response, body = self.get_json(f"/chongwufuwu/info/{record_id}", token=self.login_admin())
        self.assert_api_ok(response, body)
        self.assertEqual(int(body["data"]["id"]), int(record_id))

    def test_API_GOODS_001_goods_list_first_page(self):
        response, body = self.get_json("/chongwuyongpin/list", params={"page": 1, "limit": 5})
        self.assert_page_payload(response, body)

    def test_API_GOODS_002_goods_list_search_name(self):
        response, body = self.get_json("/chongwuyongpin/list", params={"page": 1, "limit": 5, "shangpinmingcheng": "cat"})
        self.assert_page_payload(response, body)

    def test_API_GOODS_003_goods_detail_valid_id(self):
        record_id = self.first_id("chongwuyongpin")
        response, body = self.get_json(f"/chongwuyongpin/detail/{record_id}")
        self.assert_api_ok(response, body)
        self.assertIn("jiage", body["data"])
        self.assertIn("kucun", body["data"])

    def test_API_GOODS_004_goods_detail_not_found(self):
        response, body = self.get_json("/chongwuyongpin/detail/999999")
        self.assert_empty_or_error(response, body)

    def test_API_GOODS_005_goods_stock_remind(self):
        response, body = self.get_json("/chongwuyongpin/remind/kucun/1")
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.assertIn("data", body)

    def test_API_FOSTER_001_foster_list(self):
        response, body = self.get_json("/jiyangfuwu/list", params={"page": 1, "limit": 5})
        self.assert_page_payload(response, body)

    def test_API_FOSTER_002_foster_detail(self):
        record_id = self.first_id("jiyangfuwu")
        response, body = self.get_json(f"/jiyangfuwu/detail/{record_id}")
        self.assert_api_ok(response, body)

    def test_API_FOSTER_003_foster_type_filter(self):
        response, body = self.get_json("/jiyangfuwu/list", params={"page": 1, "limit": 5, "fuwuleixing": "all-day"})
        self.assert_page_payload(response, body)

    def test_API_FOSTER_004_foster_invalid_page(self):
        response, body = self.get_json("/jiyangfuwu/list", params={"page": "abc", "limit": -1})
        self.assert_http_ok(response)
        self.assert_json(response, body)

    def test_API_ADOPT_001_adopt_list(self):
        response, body = self.get_json("/lingyangchongwu/list", params={"page": 1, "limit": 5})
        self.assert_page_payload(response, body)

    def test_API_ADOPT_002_adopt_detail(self):
        record_id = self.first_id("lingyangchongwu")
        response, body = self.get_json(f"/lingyangchongwu/detail/{record_id}")
        self.assert_api_ok(response, body)

    def test_API_ADOPT_003_adopt_status_filter(self):
        response, body = self.get_json("/lingyangchongwu/list", params={"page": 1, "limit": 5, "lingyangzhuangtai": "pending"})
        self.assert_page_payload(response, body)

    def test_API_ADOPT_004_adopt_detail_not_found(self):
        response, body = self.get_json("/lingyangchongwu/detail/999999")
        self.assert_empty_or_error(response, body)


class TestOrderAndApplyApi(ApiTestCase):
    def test_API_ORDER_001_service_order_add_success(self):
        response, body = self.post_json("/fuwudingdan/add", self.service_order_payload(), token=self.login_front())
        self.assert_api_ok(response, body)
        self.cleanup_record("fuwudingdan", body.get("data"))

    def test_API_ORDER_002_service_order_missing_required_field(self):
        response, body = self.post_json("/fuwudingdan/add", self.service_order_payload(chongwuxingming=""), token=self.login_front())
        self.assert_api_fail_cleanup("fuwudingdan", response, body)

    def test_API_ORDER_003_foster_order_add_success(self):
        response, body = self.post_json("/jiyangdingdan/add", self.foster_order_payload(), token=self.login_front())
        self.assert_api_ok(response, body)
        self.cleanup_record("jiyangdingdan", body.get("data"))

    def test_API_ORDER_004_foster_order_invalid_date(self):
        response, body = self.post_json("/jiyangdingdan/add", self.foster_order_payload(jiyangriqi="abc"), token=self.login_front())
        try:
            self.assert_http_ok(response)
            self.assert_json(response, body)
            self.assertNotEqual(body.get("code"), 0)
        finally:
            if isinstance(body, dict) and body.get("code") == 0 and isinstance(body.get("data"), int):
                self.cleanup_record("jiyangdingdan", body.get("data"))

    def test_API_ORDER_005_goods_order_add_success(self):
        response, body = self.post_json("/shangpindingdan/add", self.goods_order_payload(), token=self.login_front())
        self.assert_api_ok(response, body)
        self.cleanup_record("shangpindingdan", body.get("data"))

    def test_API_ORDER_006_goods_order_zero_quantity(self):
        response, body = self.post_json("/shangpindingdan/add", self.goods_order_payload(kucun=0), token=self.login_front())
        self.assert_api_fail_cleanup("shangpindingdan", response, body)

    def test_API_ORDER_007_goods_order_over_stock(self):
        response, body = self.post_json("/shangpindingdan/add", self.goods_order_payload(kucun=999999), token=self.login_front())
        self.assert_api_fail_cleanup("shangpindingdan", response, body)

    def test_API_APPLY_001_adopt_apply_success(self):
        response, body = self.post_json("/lingyangshenqing/add", self.apply_payload(), token=self.login_front())
        self.assert_api_ok(response, body)
        self.cleanup_record("lingyangshenqing", body.get("data"))

    def test_API_APPLY_002_adopt_apply_empty_description(self):
        response, body = self.post_json("/lingyangshenqing/add", self.apply_payload(lingyangshuoming=""), token=self.login_front())
        self.assert_api_fail_cleanup("lingyangshenqing", response, body)

    def test_API_APPLY_003_adopt_apply_duplicate(self):
        payload = self.apply_payload()
        response1, body1 = self.post_json("/lingyangshenqing/add", payload, token=self.login_front())
        self.assert_api_ok(response1, body1)
        response2, body2 = self.post_json("/lingyangshenqing/add", payload, token=self.login_front())
        self.assert_api_fail(response2, body2)
        self.cleanup_record("lingyangshenqing", body1.get("data"))
        self.cleanup_record("lingyangshenqing", body2.get("data") if isinstance(body2, dict) else None)

    def test_API_APPLY_004_adopt_apply_adopted_pet(self):
        payload = self.apply_payload()
        payload["lingyangzhuangtai"] = "adopted"
        response, body = self.post_json("/lingyangshenqing/add", payload, token=self.login_front())
        self.assert_api_fail_cleanup("lingyangshenqing", response, body)

    def test_API_APPLY_005_adopt_apply_long_description(self):
        response, body = self.post_json("/lingyangshenqing/add", self.apply_payload(lingyangshuoming="x" * 5000), token=self.login_front())
        try:
            self.assert_http_ok(response)
            self.assert_json(response, body)
        finally:
            if isinstance(body, dict) and body.get("code") == 0 and isinstance(body.get("data"), int):
                self.cleanup_record("lingyangshenqing", body.get("data"))


class TestAdminCrudAndReviewApi(ApiTestCase):
    def test_API_ADMIN_CRUD_001_service_save_success(self):
        response, body = self.post_json("/chongwufuwu/save", self.service_payload(), token=self.login_admin())
        self.assert_api_ok(response, body)
        self.cleanup_record("chongwufuwu", body.get("data"))

    def test_API_ADMIN_CRUD_002_service_save_missing_required(self):
        response, body = self.post_json("/chongwufuwu/save", self.service_payload(fuwumingcheng=""), token=self.login_admin())
        self.assert_api_fail_cleanup("chongwufuwu", response, body)

    def test_API_ADMIN_CRUD_003_service_update_success(self):
        response, body = self.post_json("/chongwufuwu/save", self.service_payload(), token=self.login_admin())
        self.assert_api_ok(response, body)
        record_id = body.get("data")
        try:
            update_response, update_body = self.post_json("/chongwufuwu/update", {"id": record_id, "jifen": 99}, token=self.login_admin())
            self.assert_api_ok(update_response, update_body)
            detail_response, detail_body = self.get_json(f"/chongwufuwu/detail/{record_id}")
            self.assert_api_ok(detail_response, detail_body)
            self.assertIn("jifen", detail_body["data"], detail_body)
            self.assertEqual(float(detail_body["data"]["jifen"]), 99.0)
        finally:
            self.cleanup_record("chongwufuwu", record_id)

    def test_API_ADMIN_CRUD_004_service_update_not_found(self):
        response, body = self.post_json("/chongwufuwu/update", {"id": 999999, "jifen": 99}, token=self.login_admin())
        self.assert_http_ok(response)
        self.assert_json(response, body)

    def test_API_ADMIN_CRUD_005_service_delete_success(self):
        response, body = self.post_json("/chongwufuwu/save", self.service_payload(), token=self.login_admin())
        self.assert_api_ok(response, body)
        record_id = body.get("data")
        delete_response, delete_body = self.post_json("/chongwufuwu/delete", [record_id], token=self.login_admin())
        self.assert_api_ok(delete_response, delete_body)
        detail_response, detail_body = self.get_json(f"/chongwufuwu/detail/{record_id}")
        self.assert_empty_or_error(detail_response, detail_body)

    def test_API_ADMIN_CRUD_006_service_delete_not_found(self):
        response, body = self.post_json("/chongwufuwu/delete", [999999], token=self.login_admin())
        self.assert_http_ok(response)
        self.assert_json(response, body)

    def test_API_ADMIN_CRUD_007_user_token_update_service_forbidden(self):
        record = self.first_record("chongwufuwu")
        original = record.get("jifen")
        try:
            response, body = self.post_json("/chongwufuwu/update", {"id": record["id"], "jifen": 1}, token=self.login_front())
            self.assert_http_ok(response)
            self.assert_json(response, body)
            detail_response, detail_body = self.get_json(f"/chongwufuwu/detail/{record['id']}")
            self.assert_api_ok(detail_response, detail_body)
            self.assertEqual(detail_body["data"].get("jifen"), original)
        finally:
            self.post_json("/chongwufuwu/update", {"id": record["id"], "jifen": original}, token=self.login_admin())

    def test_API_REVIEW_001_apply_review_pass(self):
        add_response, add_body = self.post_json("/lingyangshenqing/add", self.apply_payload(), token=self.login_front())
        self.assert_api_ok(add_response, add_body)
        record_id = add_body.get("data")
        response, body = self.post_json("/lingyangshenqing/shBatch", {"ids": [record_id], "sfsh": "yes"}, token=self.login_admin())
        self.assert_api_ok(response, body)
        self.cleanup_record("lingyangshenqing", record_id)

    def test_API_REVIEW_002_apply_review_reject(self):
        add_response, add_body = self.post_json("/lingyangshenqing/add", self.apply_payload(), token=self.login_front())
        self.assert_api_ok(add_response, add_body)
        record_id = add_body.get("data")
        response, body = self.post_json("/lingyangshenqing/shBatch", {"ids": [record_id], "sfsh": "no", "shhf": "reject"}, token=self.login_admin())
        self.assert_api_ok(response, body)
        self.cleanup_record("lingyangshenqing", record_id)

    def test_API_REVIEW_003_service_order_review_pass(self):
        add_response, add_body = self.post_json("/fuwudingdan/add", self.service_order_payload(), token=self.login_front())
        self.assert_api_ok(add_response, add_body)
        record_id = add_body.get("data")
        response, body = self.post_json("/fuwudingdan/shBatch", {"ids": [record_id], "sfsh": "yes"}, token=self.login_admin())
        self.assert_api_ok(response, body)
        self.cleanup_record("fuwudingdan", record_id)

    def test_API_REVIEW_004_review_not_found(self):
        response, body = self.post_json("/fuwudingdan/shBatch", {"ids": [999999], "sfsh": "yes"}, token=self.login_admin())
        self.assert_http_ok(response)
        self.assert_json(response, body)

    def test_API_REVIEW_005_user_token_review_forbidden(self):
        add_response, add_body = self.post_json("/fuwudingdan/add", self.service_order_payload(), token=self.login_front())
        self.assert_api_ok(add_response, add_body)
        record_id = add_body.get("data")
        response, body = self.post_json("/fuwudingdan/shBatch", {"ids": [record_id], "sfsh": "yes"}, token=self.login_front())
        self.assert_http_ok(response)
        self.assert_json(response, body)
        detail_response, detail_body = self.get_json(f"/fuwudingdan/detail/{record_id}", token=self.login_admin())
        self.assert_api_ok(detail_response, detail_body)
        self.assertNotEqual(detail_body["data"].get("sfsh"), "yes")
        self.cleanup_record("fuwudingdan", record_id)


class TestFileAndStatisticsApi(ApiTestCase):
    def upload_file_case(self, filename, content, content_type):
        before = set(self.UPLOAD_DIR.iterdir()) if self.UPLOAD_DIR.exists() else set()
        files = {"file": (filename, content, content_type)}
        response, body = self.post_form("/file/upload", token=self.login_admin(), files=files)
        after = set(self.UPLOAD_DIR.iterdir()) if self.UPLOAD_DIR.exists() else set()
        for path in after - before:
            if path.is_file():
                path.unlink()
        return response, body

    def test_API_FILE_001_upload_jpg(self):
        response, body = self.upload_file_case("pet.jpg", b"\xff\xd8\xff\xe0api-test", "image/jpeg")
        self.assert_api_ok(response, body)
        self.assertIn("file", str(body.get("data", "")))

    def test_API_FILE_002_upload_png(self):
        response, body = self.upload_file_case("pet.png", b"\x89PNG\r\n\x1a\napi-test", "image/png")
        self.assert_api_ok(response, body)

    def test_API_FILE_003_upload_exe_rejected(self):
        response, body = self.upload_file_case("test.exe", b"MZapi-test", "application/octet-stream")
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.assertNotEqual(body.get("code"), 0)

    def test_API_FILE_004_upload_large_file(self):
        response, body = self.upload_file_case("large.jpg", b"0" * (20 * 1024 * 1024), "image/jpeg")
        self.assert_http_ok(response)
        self.assert_json(response, body)

    def test_API_FILE_005_upload_empty_file(self):
        response, body = self.upload_file_case("empty.jpg", b"", "image/jpeg")
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.assertNotEqual(body.get("code"), 0)

    def test_API_FILE_006_upload_chinese_filename(self):
        response, body = self.upload_file_case("pet_photo_cn.jpg", b"\xff\xd8\xff\xe0api-test", "image/jpeg")
        self.assert_api_ok(response, body)

    def test_API_FILE_007_upload_double_extension(self):
        response, body = self.upload_file_case("a.jpg.php", b"<?php echo 1; ?>", "application/octet-stream")
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.assertNotEqual(body.get("code"), 0)

    def test_API_FILE_008_upload_path_traversal_filename(self):
        response, body = self.upload_file_case("../evil.jpg", b"\xff\xd8\xff\xe0api-test", "image/jpeg")
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.assertNotIn("..", str(body))

    def test_API_STAT_001_service_order_count(self):
        response, body = self.get_json("/fuwudingdan/count", token=self.login_admin())
        self.assert_api_ok(response, body)
        self.assertGreaterEqual(float(body.get("data", 0)), 0)

    def test_API_STAT_002_service_income_value(self):
        response, body = self.get_json("/fuwudingdan/value/fuwuleixing/jifen", token=self.login_admin())
        self.assert_api_ok(response, body)
        self.assertIsInstance(body.get("data"), list)

    def test_API_STAT_003_foster_income_value(self):
        response, body = self.get_json("/jiyangdingdan/value/fuwuleixing/jifen", token=self.login_admin())
        self.assert_api_ok(response, body)
        self.assertIsInstance(body.get("data"), list)

    def test_API_STAT_004_goods_sales_value(self):
        response, body = self.get_json("/shangpindingdan/value/shangpinleixing/jifen", token=self.login_admin())
        self.assert_api_ok(response, body)
        self.assertIsInstance(body.get("data"), list)

    def test_API_STAT_005_invalid_stat_field(self):
        response, body = self.get_json("/fuwudingdan/value/invalid/jifen", token=self.login_admin())
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.assertNotEqual(body.get("code"), 0)

    def test_API_STAT_006_goods_stock_remind(self):
        response, body = self.get_json("/chongwuyongpin/remind/kucun/1")
        self.assert_http_ok(response)
        self.assert_json(response, body)


class TestSocialForumSecurityApi(ApiTestCase):
    def test_API_SOCIAL_001_storeup_add(self):
        service = self.first_record("chongwufuwu")
        user = self.front_user()
        payload = {
            "userid": user["id"],
            "refid": service["id"],
            "tablename": "chongwufuwu",
            "name": service.get("fuwumingcheng", "api-service"),
            "picture": service.get("fuwufengmian", ""),
            "type": "1",
        }
        response, body = self.post_json("/storeup/add", payload, token=self.login_front())
        self.assert_api_ok(response, body)
        self.cleanup_record("storeup", body.get("data"))

    def test_API_SOCIAL_002_storeup_delete(self):
        service = self.first_record("chongwufuwu")
        user = self.front_user()
        add_response, add_body = self.post_json(
            "/storeup/add",
            {"userid": user["id"], "refid": service["id"], "tablename": "chongwufuwu", "name": service.get("fuwumingcheng", "api-service")},
            token=self.login_front(),
        )
        self.assert_api_ok(add_response, add_body)
        response, body = self.post_json("/storeup/delete", [add_body.get("data")], token=self.login_front())
        self.assert_api_ok(response, body)

    def test_API_SOCIAL_003_comment_add_success(self):
        service_id = self.first_id("chongwufuwu")
        user = self.front_user()
        payload = {"refid": service_id, "userid": user["id"], "nickname": user.get("xingming", "api"), "content": "good service"}
        response, body = self.post_json("/discusschongwufuwu/add", payload, token=self.login_front())
        self.assert_api_ok(response, body)
        self.cleanup_record("discusschongwufuwu", body.get("data"))

    def test_API_SOCIAL_004_comment_empty_content(self):
        service_id = self.first_id("chongwufuwu")
        user = self.front_user()
        response, body = self.post_json("/discusschongwufuwu/add", {"refid": service_id, "userid": user["id"], "content": ""}, token=self.login_front())
        self.assert_api_fail_cleanup("discusschongwufuwu", response, body)

    def test_API_SOCIAL_005_comment_xss_content(self):
        service_id = self.first_id("chongwufuwu")
        user = self.front_user()
        response, body = self.post_json(
            "/discusschongwufuwu/add",
            {"refid": service_id, "userid": user["id"], "content": "<script>alert(1)</script>"},
            token=self.login_front(),
        )
        self.assert_api_ok(response, body)
        self.cleanup_record("discusschongwufuwu", body.get("data"))

    def test_API_SOCIAL_006_comment_long_content(self):
        service_id = self.first_id("chongwufuwu")
        user = self.front_user()
        response, body = self.post_json("/discusschongwufuwu/add", {"refid": service_id, "userid": user["id"], "content": "x" * 5000}, token=self.login_front())
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.cleanup_record("discusschongwufuwu", body.get("data") if isinstance(body, dict) else None)

    def test_API_FORUM_001_forum_list(self):
        response, body = self.get_json("/forum/list", params={"page": 1, "limit": 5})
        self.assert_page_payload(response, body)

    def test_API_FORUM_002_forum_add(self):
        payload = {"title": self.unique("api_forum"), "content": "api forum content", "parentid": 0, "userid": self.front_user()["id"], "username": self.FRONT_USER}
        response, body = self.post_json("/forum/add", payload, token=self.login_front())
        self.assert_api_ok(response, body)
        self.cleanup_record("forum", body.get("data"))

    def test_API_FORUM_003_forum_empty_content(self):
        payload = {"title": self.unique("api_forum"), "content": "", "parentid": 0, "userid": self.front_user()["id"], "username": self.FRONT_USER}
        response, body = self.post_json("/forum/add", payload, token=self.login_front())
        self.assert_api_fail_cleanup("forum", response, body)

    def test_API_FORUM_004_forum_long_title(self):
        payload = {"title": "x" * 5000, "content": "api forum content", "parentid": 0, "userid": self.front_user()["id"], "username": self.FRONT_USER}
        response, body = self.post_json("/forum/add", payload, token=self.login_front())
        self.assert_http_ok(response)
        self.assert_json(response, body)
        self.cleanup_record("forum", body.get("data") if isinstance(body, dict) else None)

    def test_API_FORUM_005_chat_add(self):
        user = self.front_user()
        response, body = self.post_json("/chat/add", {"userid": user["id"], "ask": "hello", "uname": user.get("xingming", "api"), "isreply": 0}, token=self.login_front())
        self.assert_api_ok(response, body)
        self.cleanup_record("chat", body.get("data"))

    def test_API_FORUM_006_chat_empty_content(self):
        user = self.front_user()
        response, body = self.post_json("/chat/add", {"userid": user["id"], "ask": "", "uname": user.get("xingming", "api"), "isreply": 0}, token=self.login_front())
        self.assert_api_fail_cleanup("chat", response, body)

    def test_API_SEC_001_backend_page_without_token(self):
        response, body = self.get_json("/yonghu/page", params={"page": 1, "limit": 5})
        self.assert_api_fail(response, body)

    def test_API_SEC_002_user_token_order_page_isolated(self):
        response, body = self.get_json("/shangpindingdan/page", token=self.login_front(), params={"page": 1, "limit": 20})
        self.assert_page_payload(response, body)
        for row in body["data"]["list"]:
            self.assertEqual(str(row.get("zhanghao")), str(self.FRONT_USER))

    def test_API_SEC_003_user_delete_other_order_forbidden(self):
        add_response, add_body = self.post_json("/shangpindingdan/save", self.goods_order_payload(), token=self.login_admin())
        self.assert_api_ok(add_response, add_body)
        record_id = add_body.get("data")
        try:
            response, body = self.post_json("/shangpindingdan/delete", [record_id], token=self.login_front())
            self.assert_http_ok(response)
            self.assert_json(response, body)
            detail_response, detail_body = self.get_json(f"/shangpindingdan/detail/{record_id}", token=self.login_admin())
            self.assert_api_ok(detail_response, detail_body)
            self.assertIn("id", detail_body["data"], detail_body)
            self.assertEqual(int(detail_body["data"]["id"]), int(record_id))
        finally:
            self.cleanup_record("shangpindingdan", record_id)

    def test_API_SEC_004_sql_injection_parameter(self):
        response, body = self.get_json("/yonghu/list", params={"zhanghao": "' OR 1=1 --", "page": 1, "limit": 5})
        self.assert_page_payload(response, body)
        self.assertEqual(body["data"]["list"], [])

    def test_API_SEC_005_invalid_json_body(self):
        response = self.raw_request("POST", "/yonghu/login", data="{bad json", headers={"Content-Type": "application/json"})
        body = self.parse_json(response)
        self.assert_http_ok(response)
        if body is not None:
            self.assertNotEqual(body.get("code"), 0)

    def test_API_SEC_006_idor_update_other_user_forbidden(self):
        detail_response, detail_body = self.get_json("/yonghu/detail/1", token=self.login_admin())
        self.assert_api_ok(detail_response, detail_body)
        original_name = detail_body.get("data", {}).get("xingming")
        hacked_name = self.unique("hacked")
        try:
            response, body = self.post_json("/yonghu/update", {"id": 1, "xingming": hacked_name}, token=self.login_front())
            self.assert_http_ok(response)
            self.assert_json(response, body)
            check_response, check_body = self.get_json("/yonghu/detail/1", token=self.login_admin())
            self.assert_api_ok(check_response, check_body)
            self.assertNotIn("hacked", str(check_body.get("data", {})))
        finally:
            if original_name is not None:
                self.post_json("/yonghu/update", {"id": 1, "xingming": original_name}, token=self.login_admin())

    def test_API_SEC_007_not_found_path(self):
        response = self.raw_request("GET", "/not_exists_api")
        self.assertEqual(response.status_code, 404)
        self.assertNotIn("SECRET_KEY", response.text)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
