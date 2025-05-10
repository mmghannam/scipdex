### The Knapsack Problem 

In this exercise, you will be asked to implement several variants of the famous Knapsack problem.

The most popular variant of this problem is the $0-1$ knapsack, where one needs to decide which items to put into a knapsack/bag.
These items both have a weight and a value, and thus the objective is to maximize the total value we bring, keeping in mind
that the knapsack's capacity cannot be exceeded by the total weight of chosen items.

$$
\begin{align*}
\max_x      & \sum_{i \in \mathcal{I}} x_i v_i \\
\text{s.t.} & \sum_{i \in \mathcal{I}} x_i w_i \leq C\\
            & x_i \in \lbrace 0,1 \rbrace, \forall i \in \mathcal{I} 
\end{align*}
$$

<figure>
<p align="center">
<img src="skippy_knapsack.png" alt="drawing" width="400"/>
<figcaption align="center">Figure 1: Skippy undecided between taking a gold bar, a pizza slice, and the Z1 motor-driven mechanical computer.</figcaption>
</figure>

Sometimes the key to solving a real-world problem is to identify the well-known classic problem that represents them.  
Here are some examples where knapsack could be applied:
- Loading cargo in airplanes given their cost and weight
- Choosing which ads to display on a webpage, given revenue and size constraints.
- Maximizing portfolio revenue given risk and diversification constraints

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