## Primal Heuristics

Primal heuristics are ways to generate feasible solutions to an optimization problem. While not necessarily getting the best solutions, they aim to be quick. Having the ability to generate many of these solutions throughout the solving process may allow for pruning additional parts of the tree or even solve subtrees to optimality.

For more in-depth information on primal heuristics, you can look at [How to add primal heuristics](https://www.scipopt.org/doc/html/HEUR.php) at SCIP's website.

For an implementation of a heuristic in PySCIPOpt, you can look at the `SimpleRoundingHeuristic` in [test_heur.py](https://github.com/scipopt/PySCIPOpt/blob/master/tests/test_heur.py) on PySCIPOpt's GitHub repo.

### Basic structure

#### heurexec

The main code of your heuristic should go in here.

If you have successfully found a solution, you should return `{'result': pyscipopt.SCIP_RESULT.FOUNDSOL}`. PySCIPOpt parses this dictionary and signals SCIP that the heuristic was successful. 



### Supplementary material

#### Primal-dual integral 

The *primal-dual integral* (PDI) is a common measure for the strength of a primal heuristic. As we want them to generate good solutions quickly, a way to compare two different heuristics is by measuring the integral of the primal-dual gap. A heuristic that provides a fair solution very quickly will have a better PDI than another which takes much longer to generate one that is only a bit better.

Originally introduced in *Measuring the impact of primal heuristics* by Timo Berthold.

#### Matroids

Generally the easiest heuristics one can implement are greedy ones. First fit for bin packing, Nearest Neighbor for TSP, they are all characterized by being constructive and choosing the locally best option available. While this approach can be rather bad in some problems, it can be rather good in others. In fact, there are some problems where they are guaranteed to provide the optimal solution (like the Change-making problem with euros). 

This guarantee is given if one is able to detect a matroid in our problem. You can read more about Matroids [here](https://www.jeremykun.com/2014/08/26/when-greedy-algorithms-are-perfect-the-matroid/).