import unittest
from io import StringIO
from unittest.mock import patch


class TestPrintVersion(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_version(self, mock_stdout):
        from print_version import print_version
        print_version()
        self.assertIn("SCIP version", mock_stdout.getvalue(), "SCIP version is not printed")

