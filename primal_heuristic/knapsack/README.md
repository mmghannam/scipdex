## The Knapsack Problem 

In this exercise, you will be asked to implement heuristics for the Knapsack problem. If you need a reminder, you can go over the [knapsack README](modeling/knapsack/README.md) in the modeling chapter.


### Section 1: Greedy heuristic
First, let's implement a greedy heuristic. 

#### Exercise 1: LP-relaxation w/o PySCIPOpt

First, we will start with a much easier version of knapsack, where we are allowed to take fractions of items. This is called the *linear relaxation* and is solved at every node of the branch and bound tree. 

**Your task:** Write a script that returns the optimal knapsack solution for the linear relaxation without using PySCIPOpt. 

#### Exercise 2: Greedy heuristic w/o PySCIPOpt

**Your task:** Get the 

#### Exercise 3: Implementing a Primal Heuristic

Now that you have done most of the hard work, let's incorporate it into an actual heuristic that SCIP will call.  

**Your task:** Complete the KnapsackLPGreedy class in [knapsack_lp_greedy.py](knapsack_lp_greedy.py).

### Section 2: Some other heuristic