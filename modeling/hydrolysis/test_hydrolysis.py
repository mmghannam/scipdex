from pyscipopt import Model
from hydrolysis import simple_hydrolysis, complex_hydrolysis

def test_simple_hydrolysis():

    model = simple_hydrolysis(1, 1, 10)

    model.optimize()

    assert model.getObjVal() == -999999999999

def test_complex_hydrolysis():

    model = complex_hydrolysis(1, 1, [1, 2, 3], [1, 2, 3], [1, 2, 3], 10)

    model.optimize()

    assert model.getObjVal() == -999999999999