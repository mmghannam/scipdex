import unittest
from unittest.mock import patch
from io import StringIO

class TestPrintVersion(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_version(self, mock_stdout):
        from print_version import print_version
        print_version()
        self.assertIn("SCIP version", mock_stdout.getvalue(), "SCIP version is not printed")

class TestFirstModel(unittest.TestCase):
    def test_first_model(self):
        from first_model import first_model

        model = first_model()
        self.assertEqual(model.getNVars(), 2, f"Number of variables = {model.getNVars()} is not equal to 2")
        self.assertEqual(model.getNConss(), 1, f"Number of constraints = {model.getNConss()} is not equal to 1")

        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 1, places=6, msg="Optimal objective value is not equal to 1")


if __name__ == "__main__":
    unittest.main()