## 02. Modeling in PySCIPOpt

Welcome to the modeling exercises! 🚀 SCIP is one of the most versatile solvers out there for modeling. 
We will start with the basics of modeling (mixed) integer linear programs and move on to more advanced constraint types.

### Problem 1 - Knapsack 

In this first exercise, you will be asked to implement several variants of the famous Knapsack problem.

The most popular variant of this problem is the $0-1$ knapsack, where one needs to decide which items to put into a knapsack/bag.
These items both have a weight and a value, and thus the objective is to maximize the total value we bring, keeping in mind
that the knapsack's capacity cannot be exceeded by the total weight of chosen items.

<figure>
<p align="center">
<img src="skippy_knapsack.png" alt="drawing" width="400"/>
<figcaption align="center">Figure 1: Skippy undecided between taking a gold bar, a pizza slice, and the Z1 motor-driven mechanical computer.</figcaption>
</figure>

$$
\begin{align*}
\max_x      & \sum_{i \in \mathcal{I}} x_i v_i \\
\text{s.t.} & \sum_{i \in \mathcal{I}} x_i w_i \leq C\\
            & x_i \in \lbrace 0,1 \rbrace, \forall i \in \mathcal{I} 
\end{align*}
$$

As you will see with these classical problems, they . 
Sometimes the key to solving a real-world problem is to identify the well-known classic problem that represents them.  
Here are some examples where knapsack could be applied:
- a
- b
- c

#### Exercise 1.1: Knapsack problem with fractional items
Let us start with a simplified version of the classical knapsack, where instead of choosing which items to pick, we must choose which amount to pick.
Mathematically, the variable bounds go from $x_i \in \lbrace 0,1 \rbrace$ to $0 \leq x_i \leq 1$.

**Your task**: Formulate the problem described above with continuous variables 

<details>
    <summary>Hint 1</summary>
    The variable bounds can be set during variable creation with the options <code>lb</code> and <code>ub</code>, for lower bound and upper bound, respectively.
</details>

#### Exercise 1.2: 0-1 Knapsack problem
In many scenarios, we are more interested in the binary variant of the knapsack problem.

**Your task:**: Enforce integrality on the variables.

<details>
    <summary>Hint 1</summary>
    You can set the variable type during variable creation with the <code>vtype</code> option.
</details>

#### Exercise 1.3: Allow many items
**Your task:** Allow the possibility for choosing multiple copies of the same item.

<details>
    <summary>Hint 1</summary>
    Instead of the variables being binary, they can just be integer.
</details>

#### Exercise 1.4: Max 4 items in the knapsack
**Your task:** Force the solution to have at most 4 items.

#### Exercise 1.5: 3D-knapsack (nonlinear constraints)
TODO!

<!-- 
### Problem 2 - Bin-packing

# TODO
!!!! Copied from scipack !!!!

We first present the so-called "compact" formulation of the bin packing problem.
> The compactness comes from the fact the number of variables and constraints is polynomial in the number of items.

In this formulation, we have $x_{ij}$ variables that are equal to 1 if item i is packed into bin j and 0 otherwise. We also have a set of constraints that ensure that each item is packed into exactly one bin and that the total size of the items in each bin does not exceed the bin capacity. Additionally, we have a set of variables used to compute the objective value, $y_j$ that are equal to 1 if bin j is used and 0 otherwise. The objective is to minimize the number of bins used. For simplicity, we will assume that the bins have identical capacities.

The compact formulation is as follows:

$$
\begin{align*}
\text{minimize} & \quad \sum_{j=1}^{n} y_j \\
\text{subject to} & \quad \sum_{j=1}^{n} x_{ij} = 1, \quad \forall i \in \lbrace1, \ldots, m\rbrace \\
& \quad \sum_{i=1}^{m} s_i x_{ij} \leq Cy_j, \quad \forall j \in \lbrace1, \ldots, n\rbrace \\
& \quad x_{ij} \in \lbrace0, 1\rbrace, \quad \forall i \in \lbrace1, \ldots, m\rbrace, j \in \lbrace1, \ldots, n\rbrace \\
& \quad y_j \in \lbrace0, 1\rbrace, \quad \forall j \in \lbrace1, \ldots, n\rbrace
\end{align*}
$$

 -->


### Outro

