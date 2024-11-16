import pytest


def test_first_model():
    from pyscipopt import Model
    from first_model import first_model

    model = first_model()
    assert isinstance(model, Model), "Return value is not a Model instance"
    assert model.getNVars() == 2, f"Number of variables = {model.getNVars()} is not equal to 2"
    assert model.getNConss() == 1, f"Number of constraints = {model.getNConss()} is not equal to 1"

    model.optimize()

    assert model.getObjVal() == pytest.approx(1, rel=1e-6), "Optimal objective value is not equal to 1"