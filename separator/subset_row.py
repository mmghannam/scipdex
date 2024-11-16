import itertools

import pyscipopt
from pyscipopt import Model


def simple_set_partitioning() -> Model:
    model = Model()

    model.setPresolve(pyscipopt.SCIP_PARAMSETTING.OFF)
    model.setHeuristics(pyscipopt.SCIP_PARAMSETTING.OFF)
    model.setSeparating(pyscipopt.SCIP_PARAMSETTING.OFF)
    model.setParam("branching/pscost/priority", 10000000)
    model.setParam("limits/nodes", 1)

    x = {
        0: model.addVar(vtype="B", name="01", obj=1),
        1: model.addVar(vtype="B", name="x1", obj=1),
        2: model.addVar(vtype="B", name="x2", obj=1),
        3: model.addVar(vtype="B", name="x3", obj=1),
        4: model.addVar(vtype="B", name="x4", obj=1),
        5: model.addVar(vtype="B", name="x5", obj=1),
    }

    model.addCons(x[0] + x[3] + x[5] == 1)
    model.addCons(x[1] + x[3] + x[4] == 1)
    model.addCons(x[2] + x[4] + x[5] == 1)

    return model


def subset_row_separator() -> pyscipopt.Sepa:
    """
    This function implements the subset row separator algorithm for set partitioning problems.
    to test correctness, you can attach the separator to the model from simple_set_partitioning and check that it's
    returning the objective value in the end.

    TODO: find a 3-variable subset of lp solution values that sum-up to more than 1 and
    """

    class SubsetRowSeparator(pyscipopt.Sepa):
        def sepaexeclp(self):
            lp_vars, lp_solvals, *_ = self.model.getLPBranchCands()

            for i,j,k in itertools.combinations(range(len(lp_vars)), 3):
                if lp_solvals[i] + lp_solvals[j] + lp_solvals[k] > 1:
                    self.model.addCons(lp_vars[i] + lp_vars[j] + lp_vars[k] <= 1)
                    return {"result": pyscipopt.SCIP_RESULT.SEPARATED}

            return {"result": pyscipopt.SCIP_RESULT.DIDNOTFIND}

    return SubsetRowSeparator()