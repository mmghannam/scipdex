from pyscipopt import quicksum


def linear_knapsack(capacity, weights, values):
    from pyscipopt import Model
    model = Model()
    
    # TODO Implement a linear knapsack, as described in exercise 1
    x = {}
    for i in range(len(weights)):
        x[i] = model.addVar(obj=values[i])

    model.addCons(quicksum(x[i]*weights[i] for i in range(len(weights))) <= capacity)

    model.setMaximize()
    return model

def binary_knapsack(capacity, weights, values):
    from pyscipopt import Model
    model = Model()

    # TODO Implement a 0-1 knapsack, as described in exercise 2
    x = {}
    for i in range(len(weights)):
        x[i] = model.addVar(obj=values[i], vtype="B")

    model.addCons(sum(x[i]*weights[i] for i in range(len(weights))) <= capacity)

    model.setMaximize()
    return model

def integer_knapsack(capacity, weights, values):
    from pyscipopt import Model
    model = Model()

    # TODO Implement an integer knapsack, as described in exercise 3
    x = {}
    for i in range(len(weights)):
        x[i] = model.addVar(obj=values[i], vtype="I")

    model.addCons(sum(x[i]*weights[i] for i in range(len(weights))) <= capacity)

    model.setMaximize()
    return model

def limited_knapsack(capacity, weights, values, max_items):
    from pyscipopt import Model
    model = Model()

    # TODO Implement a knapsack limited to 4 items, as described in exercise 4
    x = {}
    for i in range(len(weights)):
        x[i] = model.addVar(obj=values[i], vtype="B")

    model.addCons(sum(x[i]*weights[i] for i in range(len(weights))) <= capacity)
    model.addCons(sum(x[i] for i in range(len(weights))) <= max_items)

    model.setMaximize()
    return model