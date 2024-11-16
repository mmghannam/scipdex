def first_model():
    from pyscipopt import Model

    model = Model()

    # TODO: Print the version of SCIP, which SCIP version is used?
    # maximize x + y
    # subject to
    #  x + y <= 1
    #  x, y binary

    # TODO: 1. Create variables x and y
    x = model.addVar(vtype='B', obj=1, name='x')
    y = model.addVar(vtype='B', obj=1, name='y')

    # TODO: 2. Add the constraint x + y <= 1
    model.addCons(x + y <= 1, name='c1')

    # TODO: 3. Set the objective function to maximize x + y
    model.setMaximize()

    return model

