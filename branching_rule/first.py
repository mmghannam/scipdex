import pyscipopt
from pyscipopt import Model


def first_branching_rule() -> Model:
    model = Model()

    class FirstBranchingRule(pyscipopt.Branchrule):
        def branchexeclp(self, allowaddcons):
            # get all branching candidates
            branch_cands, branch_cand_sols, *_ = self.model.getLPBranchCands()

            self.model.branchVarVal(branch_cands[0], branch_cand_sols[0])

            return {"result": pyscipopt.SCIP_RESULT.BRANCHED}

    model.includeBranchrule(FirstBranchingRule(), "FirstBranchingRule", "First branching rule",
                            priority=10000000, maxdepth=-1, maxbounddist=1)

    return model