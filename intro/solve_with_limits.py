def solve_with_limits():
    from pyscipopt import Model

    model = Model()

    # TODO: Read the problem roi2alpha3n4

    # TODO: Set the time limit to 20s, the node limit to 15, and a gap limit of 10%

    # TODO: Disable presolving and increase the aggressivness of heuristics
    
    model.optimize()
    
    # TODO: Report which of the limits terminated the solving process, and what the objective function is

    return model