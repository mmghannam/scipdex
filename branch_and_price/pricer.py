import math
from pyscipopt import Pricer, SCIP_RESULT
from pricing_knapsack import pricing_solver
from collections import defaultdict


def plot_dual_values(duals, filename=None):
    from matplotlib import pyplot as plt
    import numpy as np
    # Create figure with 3 vertically stacked subplots
    fig, axs = plt.subplots(1, 1, sharex=True)

    # colors = plt.cm.viridis(np.linspace(0, 1, len(duals)))

    for i in range(len(duals) // 10):
        axs.plot(duals[i], label=f"{i}")

    axs.set_xlabel('Iteration')
    axs.set_ylabel('Value')
    # axs.set_yscale("log")
    axs.grid(True, alpha=0.3)
    plt.tight_layout()

    # Save and show
    if filename is not None:
        plt.savefig(f"{filename}.png", bbox_inches='tight', dpi=300)
    else:
        plt.show()


class KnapsackPricer(Pricer):
    def __init__(self, sizes, capacity, constraints, branching_decisions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sizes = sizes
        self.capacity = capacity
        self.constraints = constraints
        self.branching_decisions = branching_decisions
        self.i = 0
        self.duals_at_node = defaultdict(lambda: {i: [] for i in range(len(constraints))})
        self.printed = False
        self.stable_dual = None
        self.current_node = 0

    def price(self, farkas):
        branching_decisions = self.branching_decisions[self.model.getCurrentNode().getNumber()]

        current_node = self.model.getCurrentNode().getNumber()
        if current_node != self.current_node:
            self.current_node = current_node
            self.duals_at_node[current_node] = {i: [] for i in range(len(self.constraints))}
            self.stable_dual = None
            self.i = 1

        if self.i % 10 == 0:
            print("-- iter#", self.i, "lp obj:", self.model.getLPObjVal())


        # if (current_node > 1) and not self.printed:
            # plot the duals
            # duals_at_root = self.duals_at_node[1]
            # plot_dual_values(duals_at_root)
            # self.printed = True

        dual_sol = {}
        for (cons_id, cons) in self.constraints.items():
            cons = self.model.getTransformedCons(cons)
            if farkas:
                dual_sol[cons_id] = self.model.getDualfarkasLinear(cons)
            else:
                dual_sol[cons_id] = self.model.getDualsolLinear(cons)
                self.duals_at_node[current_node][cons_id].append(dual_sol[cons_id])
                if self.i > 1:
                    alpha = 0.7
                    self.stable_dual[cons_id] = alpha * self.stable_dual[cons_id] + (1-alpha) * dual_sol[cons_id]

        if self.i == 1:
            self.stable_dual = dual_sol

        if not farkas:
            # stable_dual_sol = self.stable_dual
            stable_dual_sol = dual_sol
        else:
            stable_dual_sol = dual_sol

        min_red_cost, pattern = pricing_solver(self.sizes, self.capacity, stable_dual_sol,
                                               branching_decisions["together"], branching_decisions["apart"])
        if min_red_cost > 1e-6:  # misprice
            print("!! misprice!", min_red_cost)
            min_red_cost, pattern = pricing_solver(self.sizes, self.capacity, dual_sol,
                                                   branching_decisions["together"], branching_decisions["apart"])

        if farkas:
            min_red_cost -= 1  # in farkas' pricing the objective fn. coefficient is 0

        if min_red_cost < -1e-6:
            new_var = self.model.addVar(vtype="B", name=f"{pattern}", obj=1, pricedVar=True)
            for item in pattern:
                item_constraint = self.constraints[item]
                item_constraint = self.model.getTransformedCons(item_constraint)
                self.model.addConsCoeff(item_constraint, new_var, 1)

        return {
            'result': SCIP_RESULT.SUCCESS,
        }

    def pricerredcost(self):
        self.i += 1
        return self.price(farkas=False)

    def pricerfarkas(self):
        self.i += 1
        return self.price(farkas=True)
