## 02. Modeling in PySCIPOpt

Welcome to the modeling exercises! 🚀 SCIP is one of the most versatile solvers out there for modeling. 
We will start with the basics of modeling (mixed) integer linear programs and move on to more advanced constraint types.

### Problem 1 - Knapsack 

In this first exercise, you will be asked to implement several variants of the famous Knapsack problem.

<p align="center">
<img src="../Media/skippy_knapsack.png" alt="drawing" width="400"/>
</p>

The most popular variant of this problem is the $0-1$ knapsack, where one needs to decide which items to put into a knapsack/bag.
These items both have a weight and a value, and thus the objective is to maximize the total value we bring, keeping in mind
that the knapsack's capacity cannot be exceeded by the total weight of chosen items.

$$
\begin{align*}
\min_x      & \sum_{i \in \mathcal{I}} x_i v_i \\
\text{s.t.} & \sum_{i \in \mathcal{I}} x_i w_i \leq C\\
            & x_i \in \lbrace 0,1 \rbrace, \forall i \in \mathcal{I} 
\end{align*}
$$

#### Exercise 1.1: Knapsack problem with fractional items
Let us start with a simplified version of the classical knapsack, where instead of being forced to .
This is called the *linear relaxation* of the problem, and is essential for branch-and-bound.

**Your task**: Formulate the problem described above with continuous variables 

<details>
    <summary>Hint 1</summary>
    This way we can make hints. TODO
</details>

TODO! 

#### Exercise 1.2: 0-1 Knapsack problem
TODO! 

#### Exercise 1.3: Allow many items
TODO! 

#### Exercise 1.4: Max 4 items in the knapsack
TODO!

#### Exercise 1.5: 3D-knapsack (nonlinear constraints)
TODO!


