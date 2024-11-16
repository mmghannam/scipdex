## Primal-dual event handler

This problem is about recording the progress of the primal and dual solutions over the solving process. This might be useful for, for example, plotting the evolution of the primal and dual solutions.

### Exercise 1

Catch the correct events. You can find a list of all SCIP events <a href="https://scipopt.org/doc/html/type__event_8h.php#abdb41277158c5046b83eb5ece43e6e70"> here</a>.

**Your task:** Create an event handler that detects whenever a new primal or dual solution is found. Return the number of times this happens as a pair of integers.

<details>
    <summary>Hint 1</summary>
    The event that updates the primal dual is intuitive, but it is a bit more difficult for the dual case. The dual solution can be updated whenever an LP is solved (but might not be the best dual bound, since it might be a local LP), or whenever a node is solved (which may be solved by methods other than LP, e.g. propagation or conflict analysis). 
</details>

### Exercise 2

Now that we are stopping at the correct points in the solving process, we need to collect the solutions in a way that they remain accessible after solving. When checking the tests, we add a `data` dictionary to the `model` with `primal_log` and `dual_log` as keys, each with an empty list as items. The idea is every time a new best primal (dual) solution is found, we append [current time, solution value] to `primal_log` (`dual_log`).

**Your task:** Collect the evolution of the primal and dual solutions. Don't forget that we are only interested in the best solutions found at every point in time.

<details>
    <summary>Hint 1</summary>
    Don't forget that the logic might change depending on if it's a minimization of maximization problem.
</details>


### Exercise 3

The primal-dual integral (PDI) is an especially useful measure for determining the quality of a heuristic. It calculates the area between the dual and the primal curves, and thus a lower PDI corresponds should correspond to a better heuristic, as it manages to get good solutions sooner.  

**Your task:** Compute the primal-dual integral using the information you collected.


