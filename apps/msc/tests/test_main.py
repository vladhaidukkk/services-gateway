import io
import unittest
from contextlib import redirect_stdout

from apps.msc.app.main import main


class TestInit(unittest.TestCase):
    def test_main(self):
        output = io.StringIO()
        with redirect_stdout(output):
            main()
        captured_output = output.getvalue()
        self.assertEqual(captured_output, "Hello from MSC!\n")


if __name__ == "__main__":
    unittest.main()
