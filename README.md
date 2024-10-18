# CMSC 5724 Project1 Decision-Tree

**Source Code && Report**  for CMSC 5724 Project1

in this Project, we use Hunt's Algorithm to generate a decision tree and evaluate it on both training set and evaluation set.

> ========== EVALUATION on Training SET ==========
> Accuracy: 0.84275
> Precision: 0.79062
> Recall: 0.50093
> F1 Score: 0.61329
>
> ========== EVALUATION on Evaluation SET ==========
> Accuracy: 0.84064
> Precision: 0.77993
> Recall: 0.48946
> F1 Score: 0.60146

Meanwhile, we generate the decision tree structure in the disk as *res.txt* for storation of result.

> ========== DECISION TREE RESULT ==========
> |- martial-status is Married-civ-spouse
> L   |- education-num <= 12
> L   L   |- capital-gain <= 5013
> L   L   L   |- education-num <= 8
> L   L   L   L   |- capital-loss <= 1735
> L   L   L   R   |- age <= 35
> L   L   R   |- age <= 60
> L   L   R   L   |- education is Preschool
> L   L   R   L   L   |- INCOME <=50k
> L   L   R   L   R   |- INCOME >50k
> L   L   R   R   |- workclass is Local-gov
> L   L   R   R   L   |- INCOME <=50k
> L   L   R   R   R   |- INCOME >50k
> L   R   |- capital-gain <= 5013
> L   R   L   |- capital-loss <= 1740
> L   R   L   L   |- hours-per-week <= 30
> L   R   L   L   L   |- INCOME <=50k
> L   R   L   L   R   |- INCOME >50k
> L   R   L   R   |- capital-loss <= 1977
> L   R   L   R   L   |- INCOME >50k
> L   R   L   R   R   |- INCOME >50k
> L   R   R   |- age <= 79
> L   R   R   L   |- occupation is Farming-fishing
> L   R   R   L   L   |- INCOME >50k
> L   R   R   L   R   |- INCOME >50k
> L   R   R   R   |- INCOME >50k
> R   |- capital-gain <= 6849
> R   L   |- education-num <= 12
> R   L   L   |- capital-loss <= 2206
> R   L   L   L   |- hours-per-week <= 40
> R   L   L   R   |- fnlwgt <= 121441
> R   L   L   R   L   |- INCOME >50k
> R   L   L   R   R   |- INCOME <=50k
> R   L   R   |- hours-per-week <= 43
> R   L   R   L   |- age <= 33
> R   L   R   R   |- age <= 27
> R   R   |- age <= 19
> R   R   L   |- INCOME <=50k
> R   R   R   |- capital-gain <= 7978
> R   R   R   L   |- education-num <= 10
> R   R   R   L   L   |- INCOME <=50k
> R   R   R   L   R   |- INCOME >50k
> R   R   R   R   |- capital-gain <= 27828
> R   R   R   R   L   |- INCOME >50k
> R   R   R   R   R   |- INCOME >50k

At Last, we print the prediction result of evaluation on Evaluation SET

> ========== PREDICT RESULT OF EVALUATION SET ==========
> SAMPLE 1	: actual result - <=50k	 predicted result - <=50k	 predict True.
> SAMPLE 2	: actual result - <=50k	 predicted result - <=50k	 predict True.
> SAMPLE 3	: actual result - >50k	 predicted result - <=50k	 predict False.
> SAMPLE 4	: actual result - >50k	 predicted result - >50k	 predict True.
> SAMPLE 5	: actual result - <=50k	 predicted result - <=50k	 predict True.
> SAMPLE 6	: actual result - >50k	 predicted result - >50k	 predict True.
> SAMPLE 7	: actual result - <=50k	 predicted result - <=50k	 predict True.
> SAMPLE 8	: actual result - <=50k	 predicted result - <=50k	 predict True.
> SAMPLE 9	: actual result - >50k	 predicted result - >50k	 predict True.
> SAMPLE 10	: actual result - <=50k	 predicted result - >50k	 predict False.
