import pyscipopt


def knapsack_lp_greedy(capacity, weights, vars) -> pyscipopt.Heur:
    """
    TODO: implement a greedy heuristic for the knapsack problem using the LP solution values.
    The solution should be composed of items with the highest LP solution values that can fit in the knapsack.
    """

    class KnapsackLPGreedy(pyscipopt.Heur):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.capacity = capacity
            self.weights = weights
            self.vars = vars

        def heurexec(self, heurtiming, nodeinfeasible):
            result = pyscipopt.SCIP_RESULT.DIDNOTRUN

            # This heuristic does not run if the LP status is not optimal
            lpsolstat = self.model.getLPSolstat()
            if lpsolstat != pyscipopt.SCIP_LPSOLSTAT.OPTIMAL:
                return {"result": result}

            # transform vars to the transformed space
            self.vars = [self.model.getTransformedVar(var) for var in self.vars]

            sol = self.model.createSol(self)

            ordered_vars = sorted(list(range(len(self.vars))), key=lambda x: -self.model.getSolVal(None, self.vars[x]))

            accumulated_weight = 0
            for idx in ordered_vars:
                # check if fixed
                lpsolval = self.model.getSolVal(None, self.vars[idx])
                if self.model.isFeasEQ(lpsolval, 1.0):
                    self.model.setSolVal(sol, self.vars[idx], 1)
                    accumulated_weight += self.weights[idx]
                elif self.model.isFeasZero(lpsolval):
                    self.model.setSolVal(sol, self.vars[idx], 0)
                else:
                    if accumulated_weight + self.weights[idx] <= self.capacity:
                        self.model.setSolVal(sol, self.vars[idx], 1)
                        accumulated_weight += self.weights[idx]
                    else:
                        self.model.setSolVal(sol, self.vars[idx], 0)

            stored = self.model.trySol(sol, printreason=True)

            if stored:
                return {"result": pyscipopt.SCIP_RESULT.FOUNDSOL}
            else:
                raise Exception("Error while trying to store the solution, this should not happen, solution is feasible")

    return KnapsackLPGreedy()
