import pyscipopt

from first import first_branching_rule


def test_first_branching_rule():
    model = first_branching_rule()

    model.setPresolve(pyscipopt.SCIP_PARAMSETTING.OFF)
    model.setHeuristics(pyscipopt.SCIP_PARAMSETTING.OFF)
    model.setSeparating(pyscipopt.SCIP_PARAMSETTING.OFF)


    x1 = model.addVar(vtype='I', obj=5, lb=0, ub=100, name='x1')
    x2 = model.addVar(vtype='I', obj=6, lb=0, ub=100, name='x2')

    model.addCons(x1 + x2 <= 5, name='c1')
    model.addCons(4 * x1 + 7 * x2 <= 28, name='c2')

    model.setMaximize()

    model.optimize()

    assert model.getNNodes() == 2 # takes 4 nodes otherwise if branched on the other variable first


