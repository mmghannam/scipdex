def test_subset_row():
    from separator.subset_row import simple_set_partitioning, subset_row_separator

    model = simple_set_partitioning()
    model.includeSepa(subset_row_separator(), "subset_row_separator", "generate subset row cuts", priority=1000, freq=0)

    model.optimize()
    # assert abs(model.getObjVal() - 1) < 1e-6