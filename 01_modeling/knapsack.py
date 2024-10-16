def linear_knapsack(capacity, weights, values):
    from pyscipopt import Model
    model = Model()
    
    # TODO Implement a linear knapsack, as described in exercise 1.1
    x = {}
    for i in range(len(weights)):
        x[i] = model.addVar(obj=values[i])

    model.addCons(sum(x[i]*weights[i] for i in range(len(weights))) <= capacity)

    model.setMaximize()
    return model

def binary_knapsack(capacity, weights, values):
    from pyscipopt import Model
    model = Model()

    # TODO Implement a 0-1 knapsack, as described in exercise 1.2
    x = {}
    for i in range(len(weights)):
        x[i] = model.addVar(obj=values[i], vtype="B")

    model.addCons(sum(x[i]*weights[i] for i in range(len(weights))) <= capacity)

    model.setMaximize()
    return model

def integer_knapsack(capacity, weights, values):
    from pyscipopt import Model
    model = Model()

    # TODO Implement an integer knapsack, as described in exercise 1.3
    x = {}
    for i in range(len(weights)):
        x[i] = model.addVar(obj=values[i], vtype="I")

    model.addCons(sum(x[i]*weights[i] for i in range(len(weights))) <= capacity)

    model.setMaximize()
    return model

def limited_knapsack(capacity, weights, values):
    from pyscipopt import Model
    model = Model()

    # TODO Implement a knapsack limited to 4 items, as described in exercise 1.4
    x = {}
    for i in range(len(weights)):
        x[i] = model.addVar(obj=values[i], vtype="B")

    model.addCons(sum(x[i]*weights[i] for i in range(len(weights))) <= capacity)
    model.addCons(sum(x[i] for i in range(len(weights))) <= 4)

    model.setMaximize()
    return model

def multidimensional_knapsack(capacity, weights, values):
    from pyscipopt import Model
    model = Model()

    # TODO Implement a 3 dimensional knapsack, as described in exercise 1.5
    return model
