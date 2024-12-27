## Branching rules

After solving the LP relaxation of a node in the branch and bound tree, 
The most common type of branching rule is **variable branching**. Here, one must choose a variable which has a fractional variable in the LP solution, say $k$, and add a constraint to one of the branches imposing $k \leq \lfloor k \rfloor$ and imposing $k \geq \lceil k \rceil$ on the other.

This is not the only option however, as any partition of the search space can achieve the same result.  

For an example where different branching rules yield very different results, we refer to the extended formulation for bin-packing, detailed in the [Branch and Price](../branch_and_price/README.md) chapter.

### Exercise 1: First candidate branching

We will start with the simplest possible branching decision. After gathering all branching candidates (variables with a fractional value in the LP solution), simply pick the first one.

**Your task:** Go to `test_first.py` and fill in the implementation details.