import pytest
from pyscipopt import Model, SCIP_HEURTIMING, SCIP_PARAMSETTING


@pytest.mark.parametrize("capacity, weights", [
    (10, [1, 2, 3, 4, 5])
])
def test_knapsack_lp_greedy(capacity, weights):
    from primal_heuristic.knapsack_lp_greedy import knapsack_lp_greedy

    model = Model()

    model.setPresolve(SCIP_PARAMSETTING.OFF)
    model.setHeuristics(SCIP_PARAMSETTING.OFF)
    model.setSeparating(SCIP_PARAMSETTING.OFF)

    vars = [model.addVar(vtype="B", name=f"x{i}", obj=i) for i in range(len(weights))]
    heuristic = knapsack_lp_greedy(capacity, weights, vars)

    model.includeHeur(heuristic, "SimpleRounding", "custom heuristic implemented in python", "Y",
                      timingmask=SCIP_HEURTIMING.DURINGLPLOOP)

    model.addCons(sum(weights[i] * vars[i] for i in range(len(weights))) <= capacity)
    model.setMaximize()

    model.optimize()
