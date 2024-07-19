import io
import unittest
from contextlib import redirect_stdout

from libs.commons.lib import print_hello_app


class TestInit(unittest.TestCase):
    def test_print_hello_app(self):
        app_name = "AppName"
        output = io.StringIO()
        with redirect_stdout(output):
            print_hello_app(app_name)
        captured_output = output.getvalue()
        self.assertEqual(captured_output, f"Hello from {app_name}!\n")


if __name__ == "__main__":
    unittest.main()
