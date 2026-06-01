import os
import unittest


class RuntimeCompatibilityTests(unittest.TestCase):
    def test_django_system_check_runs(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj2.settings")

        import django
        from django.core.management import call_command

        django.setup()
        call_command("check")


if __name__ == "__main__":
    unittest.main()
