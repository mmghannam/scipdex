from pyscipopt import Model, Eventhdlr, SCIP_EVENTTYPE, Eventhdlr

class PrimalDualEventhdlr(Eventhdlr):

    def eventinit(self):
        # TODO Catch the correct events as described in exercise 1
        
        self.model.catchEvent(SCIP_EVENTTYPE.BESTSOLFOUND, self)
        self.model.catchEvent(SCIP_EVENTTYPE.LPSOLVED, self)
        self.model.catchEvent(SCIP_EVENTTYPE.NODESOLVED, self)

    def eventexec(self, event):
        # TODO Collect the primal and/or dual information as described in exercise 2

        if event.getType() == SCIP_EVENTTYPE.BESTSOLFOUND:
            self.model.data["primal_log"].append([self.model.getSolvingTime(), self.model.getPrimalbound()])

        if not self.model.data["dual_log"]:
            self.model.data["dual_log"].append([self.model.getSolvingTime(), self.model.getDualbound()])

        if self.model.getObjectiveSense() == "minimize":
            if self.model.isGT(self.model.getDualbound(), self.model.data["dual_log"][-1][1]):
                self.model.data["dual_log"].append([self.model.getSolvingTime(), self.model.getDualbound()])
        else:
            if self.model.isLT(self.model.getDualbound(), self.model.data["dual_log"][-1][1]):
                self.model.data["dual_log"].append([self.model.getSolvingTime(), self.model.getDualbound()])


def compute_pdi(primal_log, dual_log):
    pdi = 0
    # TODO Calculate the primal-dual integral as described in exercise 3


    return pdi