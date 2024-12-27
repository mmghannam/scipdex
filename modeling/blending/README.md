## Blending Problem

An important problem in the chemical industry is determining the optimal ratio of two or more substances regarding its profit, while adhering to industry-specific constraints. These constraints might be heavily nonlinear, which SCIP can thankfully (hopefully 🙂) handle.


### Exercise 1: Initial problems

Let us start with a simple scenario where the price function is linear, and the only constraints are inventory constraints.

$$
\begin{align*}
\max_x      & \sum_{i \in \mathcal{I}} x_i (s_i-c_i) \\
\text{s.t.} &  x_i \leq S_i, \forall i \in \mathcal{I} \\
            &  x_i \in \lbrace 0,1 \rbrace, \forall i \in \mathcal{I} 
\end{align*}
$$

**Your task:** Formulate this problem in PySCIPOPt.


### Exercise 2: Nonlinear pricing

Now, let's consider a scenario where the two substances are valuable when pure, even more valuable when mixed in similar proportions, and less valuable otherwise. It's plausible  might be that the mixture is somehow unstable unless it's in that profitable middle point.

$$
\begin{align*}
\max_x      & \left(\sum_{i \in \mathcal{I}} x_i\cdot\sin\left(\frac{x_i}{2}\right)\right) - \left( \sum_{i \in \mathcal{I}} x_i c_i\right)\\
\text{s.t.} \quad & x \leq S_x, \\
                  & y \leq X_y, \\
                  & x_i \in \lbrace 0,1 \rbrace, \forall i \in \mathcal{I} 
\end{align*}
$$

**Your task:** Formulate this in PySCIPOPt.

<details>
    <summary>Hint 1</summary>
    SCIP does not handle nonlinear objective functions and for this reason, neither does PySCIPOPt. However, in `pyscipopt.recipes.nonlinear` there is a `set_nonlinear_objective` function that might help in this exercise.  
</details>


### Exercise 3: Nonlinear mixings

There can also be additional constraints enforcing a lower/upper bound on ratio of constraints. If two substances are highly reactive with each other, and thus must be counterbalanced by the remaining ones.

For the exercise, assume you are given a list with substances and 
(this is slightly more interesting since they will need to somehow convert the substance name into variables)

**Your task:** Add the mixing constraints from the 

### Exercise 4: Temperature cap

You might even want to upper-bound the temperature of the reaction, to make sure that the reactors will not become damaged.

**Your task:**