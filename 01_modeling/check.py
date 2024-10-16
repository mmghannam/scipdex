import unittest
from unittest.mock import patch
from io import StringIO

class TestFirstModel(unittest.TestCase):
    def test_linear_knapsack(self):
        import knapsack

        model = knapsack.linear_knapsack()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 1000, places=6, msg="Optimal objective value is not equal to 1")

    def test_binary_knapsack(self):
        import knapsack

        model = knapsack.binary_knapsack()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 1000, places=6, msg="Optimal objective value is not equal to 1")

    def test_integer_knapsack(self):
        from pyscipopt import Model
        import knapsack

        model = knapsack.integer_knapsack()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 1000, places=6, msg="Optimal objective value is not equal to 1")

    def test_limited_knapsack(self):
        from pyscipopt import Model
        import knapsack

        model = knapsack.limited_knapsack()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 1000, places=6, msg="Optimal objective value is not equal to 1")

    def test_multidimensional_knapsack(self):
        from pyscipopt import Model
        import knapsack

        model = knapsack.multidimensional_knapsack()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 1000, places=6, msg="Optimal objective value is not equal to 1")
