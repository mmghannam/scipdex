### The Knapsack Problem 

In this exercise, you will be asked to implement heuristics for the Knapsack problem. If you need a reminder, you can go over the [knapsack README](modeling/knapsack/README.md) in the modeling chapter.


#### Exercise 1: Knapsack problem with fractional items
Let us start with a simplified version of the classical knapsack, where instead of choosing which items to pick, we must choose which amount to pick.
Mathematically, the variable bounds go from $x_i \in \lbrace 0,1 \rbrace$ to $0 \leq x_i \leq 1$.

**Your task:** Formulate the problem described above with continuous variables 

<details>
    <summary>Hint 1</summary>
    The variable bounds can be set during variable creation with the options <code>lb</code> and <code>ub</code>, for lower bound and upper bound, respectively.
</details>

#### Exercise 2: 0-1 Knapsack problem
In many scenarios, we are more interested in the binary variant of the knapsack problem.

**Your task:** Enforce integrality on the variables.

<details>
    <summary>Hint 1</summary>
    You can set the variable type during variable creation with the <code>vtype</code> option.
</details>

#### Exercise 3: Allow many items
**Your task:** Allow the possibility for choosing multiple copies of the same item.

<details>
    <summary>Hint 1</summary>
    Instead of the variables being binary, they can just be integer.
</details>

#### Exercise 4: Max `n` items in the knapsack
**Your task:** Force the solution to have at most `n` items.