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
TODO! 
**Your task:** Read the `roi2alpha3n4.mps.gz` instance.

<details>
    <summary>Hint 1</summary>
    You can use the <code>readProblem()</code> method for this.
</details>

### Exercise 4: Set parameters
TODO!
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
TODO!
**Your task**: Discover which of the parameters you set in exercise 4 terminated the solving process.

### Exercise 6: Setting emphasis modes
TODO!
**Your task:**

### Outro
If you've reached this far, congratulations!🎉 
By now, you should be able to create a basic model and query it.... 

You are now ready to take on Chapter 1, where we will be looking at modeling classic problems in the literature!
Check out the [README](../01_modeling/README.md) for the necessary information.