# CMSC 5724 Project1 Decision-Tree

**Source Code && Report**  for CMSC 5724 Project1

In this Project, we use Hunt's Algorithm to generate a decision tree in an optimized method and evaluate it on both training set and evaluation set.

The program can be executed by using the command:

```shell
 .\run.bat
```

in the root direction of the project folder in Windows or just double click the file `run.bat`, or using the command:

```shell
./run.sh
```

in the root direction of the project folder in Linux or MacOS. A Jupyter-style program can be taken from `test.ipynb`.

If you want to set the hyperparameters like `MIN_SAMPLE_SPLIT` and `MAX_DEPTH`, you can edit the file `main.py` and make the corresponding changes. The result will be output in the file `res.txt` if you execute the program by the method above.

Here's a decision tree demo generated with `MIN_SAMPLE_SPLIT=5` and `MAX_DEPTH=5`. The `L` and `R` number in front of the feature stands for the layer of the tree and the  `L`s and `R`s shows the path from the root.

```
========== DECISION TREE RESULT ==========
|- martial-status is Married-civ-spouse
L   |- education-num <= 12.5
L   L   |- capital-gain <= 5095.5
L   L   L   |- education-num <= 8.5
L   L   L   L   |- capital-loss <= 1791.5
L   L   L   R   |- age <= 35.5
L   L   R   |- age <= 60.5
L   L   R   L   |- education is Preschool
L   L   R   L   L   |- INCOME <=50k
L   L   R   L   R   |- INCOME >50k
L   L   R   R   |- workclass is Local-gov
L   L   R   R   L   |- INCOME <=50k
L   L   R   R   R   |- INCOME >50k
L   R   |- capital-gain <= 5095.5
L   R   L   |- capital-loss <= 1782.5
L   R   L   L   |- hours-per-week <= 31.0
L   R   L   L   L   |- INCOME <=50k
L   R   L   L   R   |- INCOME >50k
L   R   L   R   |- capital-loss <= 1989.5
L   R   L   R   L   |- INCOME >50k
L   R   L   R   R   |- INCOME >50k
L   R   R   |- age <= 84.5
L   R   R   L   |- occupation is Farming-fishing
L   R   R   L   L   |- INCOME >50k
L   R   R   L   R   |- INCOME >50k
L   R   R   R   |- INCOME >50k
R   |- capital-gain <= 7073.5
R   L   |- education-num <= 12.5
R   L   L   |- capital-loss <= 2218.5
R   L   L   L   |- hours-per-week <= 40.5
R   L   L   R   |- fnlwgt <= 125450.5
R   L   L   R   L   |- INCOME >50k
R   L   L   R   R   |- INCOME <=50k
R   L   R   |- hours-per-week <= 43.5
R   L   R   L   |- age <= 33.5
R   L   R   R   |- age <= 27.5
R   R   |- age <= 20.0
R   R   L   |- INCOME <=50k
R   R   R   |- capital-gain <= 8296.0
R   R   R   L   |- education-num <= 11.5
R   R   R   L   L   |- INCOME <=50k
R   R   R   L   R   |- INCOME >50k
R   R   R   R   |- capital-gain <= 30961.5
R   R   R   R   L   |- INCOME >50k
R   R   R   R   R   |- INCOME >50k
```

For example,  `L   R   |- capital-gain <= 5095.5` stands for the left node of the root and the right node of the node above is decisioning whether `capital-gain` is smaller than or equals `5095.5`. For non-numeric features, the node decision is based on `is` or `is not`.

At Last, we print the prediction result of evaluation on Evaluation SET. Here's only part of the output.

```
========== PREDICT RESULT OF EVALUATION SET ==========

SAMPLE 1	: actual result - <=50k	 predicted result - <=50k	 predict True.
SAMPLE 2	: actual result - <=50k	 predicted result - <=50k	 predict True.
SAMPLE 3	: actual result - >50k	 predicted result - <=50k	 predict False.
SAMPLE 4	: actual result - >50k	 predicted result - >50k	 predict True.
SAMPLE 5	: actual result - <=50k	 predicted result - <=50k	 predict True.
SAMPLE 6	: actual result - >50k	 predicted result - >50k	 predict True.
SAMPLE 7	: actual result - <=50k	 predicted result - <=50k	 predict True.
SAMPLE 8	: actual result - <=50k	 predicted result - <=50k	 predict True.
SAMPLE 9	: actual result - >50k	 predicted result - >50k	 predict True.
SAMPLE 10	: actual result - <=50k	 predicted result - >50k	 predict False.
```
