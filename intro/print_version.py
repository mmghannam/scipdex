def print_version():
    from pyscipopt import Model

    # Create a new model
    model = Model()
    model.redirectOutput()

    # TODO: Print the version of SCIP, which SCIP version is used?
    model.printVersion()