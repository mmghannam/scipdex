import unittest
from unittest.mock import patch
from io import StringIO
from print_version import print_version

class TestPrintVersion(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_version(self, mock_stdout):
        print_version()
        assert "SCIP version" in mock_stdout.getvalue(), "SCIP version is not printed"


if __name__ == "__main__":
    unittest.main()