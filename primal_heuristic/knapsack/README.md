## The Knapsack Problem 

In this exercise, you will be asked to implement heuristics for the Knapsack problem. If you need a reminder, you can go over the [knapsack README](../../modeling/knapsack/README.md) in the modeling chapter. For the specifics of implementing a SCIP heuristic, check the [README](../README.md) of the primal_heuristics chapter.


### Section 1: Greedy heuristic

#### Exercise 1: LP-relaxation w/o PySCIPOpt

First, we will start with a much easier version of knapsack, where we are allowed to take fractions of items. This is called the *linear relaxation* and is usually solved at every node of the branch and bound tree. 

**Your task:** Write a script which returns the optimal knapsack solution for the linear relaxation without using PySCIPOpt. 

<details>
    <summary>Hint 1</summary>
    If possible, you would like to fill the knapsack with the item with highest *value density* (value/weight). There are two options when you do this. Either the knapsack cannot fit the entire item, and the linear relaxation allows you to fill the knapsack to completion with a portion of the item, or you can fit the entire item, and you just move to the item with the next highest value density.
</details>

#### Exercise 2: Greedy heuristic w/o PySCIPOpt

We can now implement the greedy heuristic for the integer variant of knapsack. It follows the same strategy until it cannot fit an item into the knapsack, and moves to the item with the next highest value density, continuing until the knapsack is full or there are no more items.

**Your task:** Write a script which implements this strategy.

#### Exercise 3: Implementing a Primal Heuristic

Now that you have done most of the hard work, let's incorporate it into an actual heuristic that SCIP will call.  

**Your task:** Complete the KnapsackLPGreedy class in [knapsack_lp_greedy.py](knapsack_lp_greedy.py).

<details>
    <summary>Hint 1</summary>
    
</details>

### Section 2: Some other heuristic