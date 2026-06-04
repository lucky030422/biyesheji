import os
import subprocess
import sys
import unittest


class RuntimeCompatibilityTests(unittest.TestCase):
    def test_django_system_check_runs(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj2.settings")

        import django
        from django.core.management import call_command

        django.setup()
        call_command("check")

    def test_manage_check_does_not_emit_startup_debug_output(self):
        result = subprocess.run(
            [sys.executable, "manage.py", "check"],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("tableName============>", result.stdout)
        self.assertNotIn("mysql 127.0.0.1", result.stdout)


if __name__ == "__main__":
    unittest.main()
