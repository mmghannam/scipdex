import unittest
from unittest.mock import patch
from io import StringIO

class TestKnapsack(unittest.TestCase):

    capacity = 31
    v        = [103, 199, 112, 15, 71, 135, 129, 108, 82, 127, 96, 154, 60, 134, 40]
    w        = [5, 3, 2, 10, 5, 9, 10, 3, 5, 2, 2, 6, 8, 9, 2]

    def test_linear_knapsack(self):
        import knapsack

        model = knapsack.linear_knapsack(self.capacity, self.w, self.v)

        model.hideOutput()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 2056.333333, places=6, msg="Optimal objective value is not equal to 2056.333")

    def test_binary_knapsack(self):
        import knapsack

        model = knapsack.binary_knapsack(self.capacity, self.w, self.v)

        model.hideOutput()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 1021, places=6, msg="Optimal objective value is not equal to 1020")

    def test_integer_knapsack(self):
        import knapsack

        model = knapsack.integer_knapsack(self.capacity, self.w, self.v)

        model.hideOutput()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 2045, places=6, msg="Optimal objective value is not equal to 2045")

    def test_limited_knapsack(self):
        import knapsack

        model = knapsack.limited_knapsack(self.capacity, self.w, self.v)

        model.hideOutput()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 622, places=6, msg="Optimal objective value is not equal to 622")

    def test_multidimensional_knapsack(self):
        import knapsack

        model = knapsack.multidimensional_knapsack(self.capacity, self.w, self.v)

        model.hideOutput()
        model.optimize()

        self.assertAlmostEqual(model.getObjVal(), 1000, places=6, msg="Optimal objective value is not equal to 1")

unittest.main()