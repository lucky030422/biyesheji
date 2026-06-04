import base64
import json
import os
import unittest


class AuthTokenTests(unittest.TestCase):
    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj2.settings")

        import django

        django.setup()

    def test_generated_token_payload_is_base64_encoded_json(self):
        from util.auth import Auth

        class DummyModel:
            __tablename__ = "users"

        params = {"id": 1, "username": "admin", "password": "secret"}
        token = Auth().get_token(DummyModel, params)

        payload = json.loads(base64.b64decode(token).decode("utf-8"))

        self.assertEqual(payload["tablename"], "users")
        self.assertEqual(payload["params"], params)

    def test_get_token_info_decodes_generated_token(self):
        from util.auth import Auth

        class DummyModel:
            __tablename__ = "users"

        class DummyRequest:
            META = {}

        params = {"id": 1, "username": "admin"}
        request = DummyRequest()
        request.META["HTTP_TOKEN"] = Auth().get_token(DummyModel, params)

        self.assertEqual(
            Auth().getTokenInfo(request),
            {"tablename": "users", "params": params},
        )


if __name__ == "__main__":
    unittest.main()
