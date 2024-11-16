# SCIPDex  

<img src="SCIPDex.svg" align="right" width="500px">

A collection of interactive exercises to get you started (and more) with [PySCIPOpt](https://github.com/scipopt/PySCIPOpt).
It is designed to be used along with the [PySCIPOpt documentation](https://scipopt.github.io/PySCIPOpt/docs/html/index.html).  

The exercises are split into folders by topic. Each folder contains a README.md file describing the exercises and python files with TODOs. Each folder has a `check.py` file that checks if the exercises are correctly solved.

## Installation
The exercises depend only on PySCIPOpt (and its dependencies) and pytest. You can install them with:
```bash
pip install -r requirements.txt
```
for other ways of installing PySCIPOPt, please refer to the [PySCIPOpt documentation](https://pyscipopt.readthedocs.io/en/latest/install.html).

## Getting Started

Now you're ready to start the exercises 🚀 The repository is divided into chapters, each containing multiple problems. In the chapter there is a README describing each of the problems, and in each of the problems there is a README describing the problem in detail and the exercises to be completed. Besides this README, the problem folder also has a `[problem].py` file to solve the exercises and a `check.py` file for testing your solution. Here is a brief description of each chapter:

- modeling: An introduction to PySCIPOpt and its more elementary functionalities.
- event_handler: Unlocking the ability to interrupt the solving process when a predetermined event is caught, and executing user-code.

We recommend starting by going to [intro](intro) and following the instructions in the [README.md](intro/README.md) file.


## Contributing
If you find any issues or have suggestions for improvements, please open an [issue](https://github.com/mmghannam/scipdex/issues/new/choose) or a pull request. Thank you!
