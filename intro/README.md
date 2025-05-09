## 00. Introduction to PySCIPOpt

Welcome to SCIPDex! let's get started with the first exercise 🚀

### Exercise 1: Print SCIP version used
Go to [00_intro/print_version.py](print_version.py) and complete the TODOs.
You can look for the method to use in the [PySCIPOpt documentation](https://pyscipopt.readthedocs.io).


### Exercise 2: Create your first SCIP model
Go to [00_intro/first_model.py](first_model.py) and implement the following model:

$$
\begin{align*}
\max_{x,y}  \quad & x + y \\
\text{s.t.} \quad & x + y \leq 1 \\
                  & x, y \in \lbrace 0,1 \rbrace
\end{align*}
$$

Refer to the [docs](https://pyscipopt.readthedocs.io/en/latest/tutorials/model.html#create-a-model-variables-and-constraints) for help.


### Exercise 3: Read a problem from a file

PySCIPOpt also allows you to read problems, making it easier to test your code with different models, and not having the need to model them.

**Your task:** Read the `roi2alpha3n4.mps.gz` instance.

<details>
    <summary>Hint 1</summary>
    You can use the <code>readProblem()</code> method for this.
</details>

### Exercise 4: Set parameters

Sometimes you might not be interested in solving the model to optimality, or there might be some time limit you must respect. It's easy to impose these in PySCIPOpt!

You can see the full list of SCIP parameters in [here](https://www.scipopt.org/doc/html/PARAMETERS.php).

**Your task:** Optimize the model from exercise 3 with the following parameters

|  Parameter | Value |
|------------|-------|
| Time limit |  20   | 
| Node limit |  15   | 
| Gap limit  |  10%  | 

<details>
    <summary>Hint 1</summary>
    You can find the (very extensive) list of SCIP parameters <a href="https://www.scipopt.org/doc/html/PARAMETERS.php">here</a>.
</details>

### Exercise 5: Query solution and model stats

After solving the model, you can check some of its statistics. For example, it's possible to see the gap (after solving), see the values of the variables in the best solution, and much more.

**Your task**: Discover which of the parameters you set in exercise 4 terminated the solving process, and check the objective function.

<details>
    <summary>Hint 1</summary>
    It's also possible to see a lot of information about the run by using `model.writeStatistics(filename.stats)`
</details>

### Exercise 6: Setting emphasis modes
s
Optimization solvers are very complex, full of interacting components focusing on different parts of the solving process. While one instance might benefit heavily from presolving (essentially, ways of simplifying the problem), there might be another for which heuristics (methods to generate feasible solutions) help a lot.

Most solvers allow users to change the focus of its solving, so if you know characteristics of your instance, then you might hint that to the solver.  

**Your task:** Disable presolving and increase the focus of heuristics to the maximum.

### Outro
If you've reached this far, congratulations!🎉 
By now, you should be able to create a basic model and query it.... 

You are now ready to take on Chapter 1, where we will be looking at modeling classic problems in the literature!
Check out the [README](../01_modeling/README.md) for the necessary information.