
import pytest

@pytest.mark.parametrize("capacity, weights, values, expected", [
    (0, [1, 2, 3], [6, 5, 4], 0),
    (3, [1, 2, 3], [1, 5, 6], 7.5),
    (10, [1, 2, 3], [4, 5, 6], 40),
])
def test_linear_knapsack(capacity, weights, values, expected):
    from pyscipopt import Model
    from knapsack import linear_knapsack

    model = linear_knapsack(capacity, weights, values)
    assert isinstance(model, Model), "Return value is not a Model instance"
    assert model.getNVars() == 3, f"Number of variables = {model.getNVars()} is not equal to 3"
    assert model.getNConss() == 1, f"Number of constraints = {model.getNConss()} is not equal to 1"

    model.optimize()

    assert model.getObjVal() == pytest.approx(expected, rel=1e-6), "Optimal objective value is not equal to 15"

@pytest.mark.parametrize("capacity, weights, values, expected", [
    (0, [1, 2, 3], [6, 5, 4], 0),
    (3, [1, 2, 3], [1, 5, 6], 6),
    (10, [1, 2, 3], [4, 5, 6], 15),
])
def test_binary_knapsack(capacity, weights, values, expected):
    from pyscipopt import Model
    from knapsack import binary_knapsack

    model = binary_knapsack(capacity, weights, values)
    assert isinstance(model, Model), "Return value is not a Model instance"
    assert model.getNVars() == 3, f"Number of variables = {model.getNVars()} is not equal to 3"
    assert model.getNConss() == 1, f"Number of constraints = {model.getNConss()} is not equal to 1"

    model.optimize()

    assert model.getObjVal() == pytest.approx(expected, rel=1e-6), "Optimal objective value is not equal to 15"

@pytest.mark.parametrize("capacity, weights, values, expected", [
    (0, [1, 2, 3], [6, 5, 4], 0),
    (3, [1, 2, 3], [1, 5, 6], 6),
    (10, [1, 2, 3], [4, 5, 6], 40),
])
def test_integer_knapsack(capacity, weights, values, expected):
    from pyscipopt import Model
    from knapsack import integer_knapsack

    model = integer_knapsack(capacity, weights, values)
    assert isinstance(model, Model), "Return value is not a Model instance"
    assert model.getNVars() == 3, f"Number of variables = {model.getNVars()} is not equal to 3"
    assert model.getNConss() == 1, f"Number of constraints = {model.getNConss()} is not equal to 1"

    model.optimize()

    assert model.getObjVal() == pytest.approx(expected, rel=1e-6), "Optimal objective value is not equal to 15"


@pytest.mark.parametrize("capacity, weights, values, max_items, expected", [
    (10, [1, 2, 3], [4, 5, 6], 0, 0),
    (10, [1, 2, 3], [4, 5, 6], 1, 6),
    (10, [1, 2, 3], [4, 5, 6], 2, 11),
])
def test_limited_knapsack(capacity, weights, values, max_items, expected):
    from pyscipopt import Model
    from knapsack import limited_knapsack

    model = limited_knapsack(capacity, weights, values, max_items)
    assert isinstance(model, Model), "Return value is not a Model instance"
    assert model.getNVars() == 3, f"Number of variables = {model.getNVars()} is not equal to 3"
    assert model.getNConss() == 2, f"Number of constraints = {model.getNConss()} is not equal to 1"

    model.optimize()

    assert model.getObjVal() == pytest.approx(expected, rel=1e-6), "Optimal objective value is not correct"
