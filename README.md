# CMSC 5724 Project1 Decision-Tree

**Source Code && Report**  for CMSC 5724 Project1

in this Project, we use Hunt's Algorithm to generate a decision tree and evaluate it on both training set and evaluation set.

```
EVALUATION on Training SET
Accuracy: 0.86718
Precision: 0.79779
Recall: 0.62480
F1 Score: 0.70078


EVALUATION on Evaluation SET
Accuracy: 0.85604
Precision: 0.76505
Recall: 0.59757
F1 Score: 0.67102
```

Meanwhile, we generate the decision tree structure in the disk as *res.txt* for storation of result.

```
========== DECISION TREE RESULT ==========
|- martial-status is Married-civ-spouse
L   |- education-num <= 12.5
L   L   |- capital-gain <= 5095.5
L   L   L   |- education-num <= 8.5
L   L   L   L   |- capital-loss <= 1791.5
L   L   L   L   L   |- age <= 36.5
L   L   L   L   L   L   |- occupation is Tech-support
L   L   L   L   L   L   L   |- INCOME <=50k
L   L   L   L   L   L   R   |- hours-per-week <= 49.0
L   L   L   L   L   L   R   L   |- education is 12th
L   L   L   L   L   L   R   L   L   |- occupation is Sales
L   L   L   L   L   L   R   L   L   L   |- INCOME >50k
L   L   L   L   L   L   R   L   L   R   |- INCOME <=50k
L   L   L   L   L   L   R   L   R   |- occupation is Adm-clerical
L   L   L   L   L   L   R   R   |- relationship is Not-in-family
L   L   L   L   L   L   R   R   L   |- INCOME >50k
L   L   L   L   L   L   R   R   R   |- education is 5th-6th
L   L   L   L   L   R   |- education-num <= 5.5
L   L   L   L   L   R   L   |- hours-per-week <= 49.5
L   L   L   L   L   R   L   L   |- workclass is Self-emp-inc
L   L   L   L   L   R   L   L   L   |- INCOME <=50k
L   L   L   L   L   R   L   L   R   |- workclass is Federal-gov
L   L   L   L   L   R   L   L   R   L   |- INCOME >50k
L   L   L   L   L   R   L   L   R   R   |- INCOME <=50k
L   L   L   L   L   R   L   R   |- capital-gain <= 4164.0
L   L   L   L   L   R   L   R   L   |- occupation is Other-service
L   L   L   L   L   R   L   R   R   |- INCOME >50k
L   L   L   L   L   R   R   |- fnlwgt <= 366223.0
L   L   L   L   L   R   R   L   |- age <= 65.5
L   L   L   L   L   R   R   L   L   |- fnlwgt <= 198384.0
L   L   L   L   L   R   R   L   R   |- INCOME <=50k
L   L   L   L   L   R   R   R   |- fnlwgt <= 439534.0
L   L   L   L   L   R   R   R   L   |- fnlwgt <= 420075.5
L   L   L   L   L   R   R   R   L   L   |- INCOME <=50k
L   L   L   L   L   R   R   R   L   R   |- INCOME >50k
L   L   L   L   L   R   R   R   R   |- workclass is State-gov
L   L   L   L   L   R   R   R   R   L   |- INCOME >50k
L   L   L   L   L   R   R   R   R   R   |- INCOME <=50k
L   L   L   L   R   |- capital-loss <= 1989.5
L   L   L   L   R   L   |- race is Amer-Indian-Eskimo
L   L   L   L   R   L   L   |- INCOME <=50k
L   L   L   L   R   L   R   |- workclass is Local-gov
L   L   L   L   R   L   R   L   |- INCOME <=50k
L   L   L   L   R   L   R   R   |- INCOME >50k
L   L   L   L   R   R   |- INCOME <=50k
L   L   L   R   |- age <= 35.5
L   L   L   R   L   |- capital-loss <= 1794.0
L   L   L   R   L   L   |- age <= 29.5
L   L   L   R   L   L   L   |- age <= 24.5
L   L   L   R   L   L   L   L   |- occupation is Transport-moving
L   L   L   R   L   L   L   L   L   |- fnlwgt <= 332860.0
L   L   L   R   L   L   L   L   L   L   |- INCOME <=50k
L   L   L   R   L   L   L   L   L   R   |- INCOME >50k
L   L   L   R   L   L   L   L   R   |- fnlwgt <= 542762.5
L   L   L   R   L   L   L   L   R   L   |- INCOME <=50k
L   L   L   R   L   L   L   L   R   R   |- INCOME >50k
L   L   L   R   L   L   L   R   |- education is HS-grad
L   L   L   R   L   L   L   R   L   |- occupation is Prof-specialty
L   L   L   R   L   L   L   R   R   |- fnlwgt <= 291086.0
L   L   L   R   L   L   R   |- education is HS-grad
L   L   L   R   L   L   R   L   |- hours-per-week <= 52.5
L   L   L   R   L   L   R   L   L   |- race is Black
L   L   L   R   L   L   R   L   R   |- race is White
L   L   L   R   L   L   R   L   R   L   |- INCOME <=50k
L   L   L   R   L   L   R   L   R   R   |- INCOME >50k
L   L   L   R   L   L   R   R   |- fnlwgt <= 157762.5
L   L   L   R   L   L   R   R   L   |- fnlwgt <= 27233.5
L   L   L   R   L   L   R   R   L   L   |- INCOME >50k
L   L   L   R   L   L   R   R   L   R   |- INCOME <=50k
L   L   L   R   L   L   R   R   R   |- occupation is Exec-managerial
L   L   L   R   L   L   R   R   R   L   |- INCOME >50k
L   L   L   R   L   L   R   R   R   R   |- INCOME <=50k
L   L   L   R   L   R   |- capital-loss <= 1989.5
L   L   L   R   L   R   L   |- age <= 24.0
L   L   L   R   L   R   L   L   |- INCOME <=50k
L   L   L   R   L   R   L   R   |- workclass is State-gov
L   L   L   R   L   R   L   R   L   |- INCOME <=50k
L   L   L   R   L   R   L   R   R   |- occupation is Transport-moving
L   L   L   R   L   R   L   R   R   L   |- INCOME <=50k
L   L   L   R   L   R   L   R   R   R   |- INCOME >50k
L   L   L   R   L   R   R   |- occupation is Other-service
L   L   L   R   L   R   R   L   |- INCOME >50k
L   L   L   R   L   R   R   R   |- INCOME <=50k
L   L   L   R   R   |- capital-loss <= 1782.5
L   L   L   R   R   L   |- hours-per-week <= 34.5
L   L   L   R   R   L   L   |- relationship is Wife
L   L   L   R   R   L   L   L   |- occupation is Exec-managerial
L   L   L   R   R   L   L   L   L   |- hours-per-week <= 31.0
L   L   L   R   R   L   L   L   L   L   |- INCOME >50k
L   L   L   R   R   L   L   L   L   R   |- INCOME <=50k
L   L   L   R   R   L   L   L   R   |- education-num <= 10.5
L   L   L   R   R   L   L   L   R   L   |- INCOME <=50k
L   L   L   R   R   L   L   L   R   R   |- INCOME >50k
L   L   L   R   R   L   L   R   |- occupation is Tech-support
L   L   L   R   R   L   L   R   L   |- age <= 51.5
L   L   L   R   R   L   L   R   L   L   |- INCOME >50k
L   L   L   R   R   L   L   R   L   R   |- INCOME <=50k
L   L   L   R   R   L   L   R   R   |- education is HS-grad
L   L   L   R   R   L   R   |- education is HS-grad
L   L   L   R   R   L   R   L   |- occupation is Exec-managerial
L   L   L   R   R   L   R   L   L   |- workclass is Self-emp-not-inc
L   L   L   R   R   L   R   L   L   L   |- INCOME <=50k
L   L   L   R   R   L   R   L   L   R   |- INCOME >50k
L   L   L   R   R   L   R   L   R   |- workclass is Federal-gov
L   L   L   R   R   L   R   L   R   L   |- INCOME >50k
L   L   L   R   R   L   R   L   R   R   |- INCOME <=50k
L   L   L   R   R   L   R   R   |- workclass is Self-emp-not-inc
L   L   L   R   R   L   R   R   L   |- fnlwgt <= 353260.0
L   L   L   R   R   L   R   R   L   L   |- INCOME <=50k
L   L   L   R   R   L   R   R   L   R   |- INCOME >50k
L   L   L   R   R   L   R   R   R   |- occupation is Exec-managerial
L   L   L   R   R   L   R   R   R   L   |- INCOME >50k
L   L   L   R   R   L   R   R   R   R   |- INCOME <=50k
L   L   L   R   R   R   |- capital-loss <= 1989.5
L   L   L   R   R   R   L   |- age <= 66.5
L   L   L   R   R   R   L   L   |- capital-loss <= 1894.5
L   L   L   R   R   R   L   L   L   |- INCOME >50k
L   L   L   R   R   R   L   L   R   |- workclass is Local-gov
L   L   L   R   R   R   L   L   R   L   |- INCOME >50k
L   L   L   R   R   R   L   L   R   R   |- INCOME >50k
L   L   L   R   R   R   L   R   |- INCOME <=50k
L   L   L   R   R   R   R   |- capital-loss <= 2161.5
L   L   L   R   R   R   R   L   |- INCOME <=50k
L   L   L   R   R   R   R   R   |- capital-loss <= 2176.5
L   L   L   R   R   R   R   R   L   |- INCOME >50k
L   L   L   R   R   R   R   R   R   |- capital-loss <= 2212.5
L   L   L   R   R   R   R   R   R   L   |- INCOME <=50k
L   L   L   R   R   R   R   R   R   R   |- INCOME >50k
L   L   R   |- age <= 60.5
L   L   R   L   |- education is Preschool
L   L   R   L   L   |- INCOME <=50k
L   L   R   L   R   |- INCOME >50k
L   L   R   R   |- workclass is Local-gov
L   L   R   R   L   |- INCOME <=50k
L   L   R   R   R   |- occupation is Protective-serv
L   L   R   R   R   L   |- INCOME <=50k
L   L   R   R   R   R   |- capital-gain <= 9976.0
L   L   R   R   R   R   L   |- education is Assoc-voc
L   L   R   R   R   R   L   L   |- INCOME >50k
L   L   R   R   R   R   L   R   |- INCOME >50k
L   L   R   R   R   R   R   |- capital-gain <= 10585.5
L   L   R   R   R   R   R   L   |- INCOME <=50k
L   L   R   R   R   R   R   R   |- fnlwgt <= 34689.5
L   L   R   R   R   R   R   R   L   |- INCOME <=50k
L   L   R   R   R   R   R   R   R   |- INCOME >50k
L   R   |- capital-gain <= 5095.5
L   R   L   |- capital-loss <= 1782.5
L   R   L   L   |- hours-per-week <= 31.0
L   R   L   L   L   |- relationship is Wife
L   R   L   L   L   L   |- fnlwgt <= 271215.0
L   R   L   L   L   L   L   |- fnlwgt <= 99739.5
L   R   L   L   L   L   L   L   |- education is Masters
L   R   L   L   L   L   L   L   L   |- INCOME >50k
L   R   L   L   L   L   L   L   R   |- hours-per-week <= 21.0
L   R   L   L   L   L   L   L   R   L   |- INCOME <=50k
L   R   L   L   L   L   L   L   R   R   |- INCOME >50k
L   R   L   L   L   L   L   R   |- occupation is Other-service
L   R   L   L   L   L   L   R   L   |- INCOME <=50k
L   R   L   L   L   L   L   R   R   |- age <= 43.0
L   R   L   L   L   L   L   R   R   L   |- INCOME >50k
L   R   L   L   L   L   L   R   R   R   |- INCOME >50k
L   R   L   L   L   L   R   |- INCOME <=50k
L   R   L   L   L   R   |- education-num <= 14.5
L   R   L   L   L   R   L   |- age <= 32.5
L   R   L   L   L   R   L   L   |- occupation is Other-service
L   R   L   L   L   R   L   R   |- occupation is Tech-support
L   R   L   L   L   R   L   R   L   |- INCOME >50k
L   R   L   L   L   R   L   R   R   |- occupation is Sales
L   R   L   L   L   R   R   |- age <= 67.5
L   R   L   L   L   R   R   L   |- occupation is Prof-specialty
L   R   L   L   L   R   R   L   L   |- capital-gain <= 1890.5
L   R   L   L   L   R   R   L   L   L   |- INCOME >50k
L   R   L   L   L   R   R   L   L   R   |- INCOME <=50k
L   R   L   L   L   R   R   L   R   |- INCOME <=50k
L   R   L   L   L   R   R   R   |- INCOME <=50k
L   R   L   L   R   |- age <= 28.5
L   R   L   L   R   L   |- age <= 25.5
L   R   L   L   R   L   L   |- hours-per-week <= 43.5
L   R   L   L   R   L   L   L   |- workclass is Self-emp-inc
L   R   L   L   R   L   L   L   L   |- INCOME >50k
L   R   L   L   R   L   L   L   R   |- fnlwgt <= 401760.0
L   R   L   L   R   L   L   L   R   L   |- INCOME <=50k
L   R   L   L   R   L   L   L   R   R   |- INCOME >50k
L   R   L   L   R   L   L   R   |- fnlwgt <= 312041.5
L   R   L   L   R   L   L   R   L   |- occupation is Exec-managerial
L   R   L   L   R   L   L   R   L   L   |- INCOME >50k
L   R   L   L   R   L   L   R   L   R   |- INCOME <=50k
L   R   L   L   R   L   L   R   R   |- INCOME >50k
L   R   L   L   R   L   R   |- relationship is Wife
L   R   L   L   R   L   R   L   |- race is White
L   R   L   L   R   L   R   L   L   |- education is Masters
L   R   L   L   R   L   R   L   L   L   |- INCOME <=50k
L   R   L   L   R   L   R   L   L   R   |- INCOME >50k
L   R   L   L   R   L   R   L   R   |- INCOME <=50k
L   R   L   L   R   L   R   R   |- occupation is Sales
L   R   L   L   R   L   R   R   L   |- fnlwgt <= 266229.0
L   R   L   L   R   L   R   R   L   L   |- INCOME >50k
L   R   L   L   R   L   R   R   L   R   |- INCOME <=50k
L   R   L   L   R   L   R   R   R   |- fnlwgt <= 62036.5
L   R   L   L   R   R   |- capital-gain <= 3120.0
L   R   L   L   R   R   L   |- occupation is Exec-managerial
L   R   L   L   R   R   L   L   |- capital-loss <= 629.0
L   R   L   L   R   R   L   L   L   |- workclass is Self-emp-not-inc
L   R   L   L   R   R   L   L   L   L   |- INCOME >50k
L   R   L   L   R   R   L   L   L   R   |- INCOME >50k
L   R   L   L   R   R   L   L   R   |- INCOME <=50k
L   R   L   L   R   R   L   R   |- occupation is Prof-specialty
L   R   L   L   R   R   L   R   L   |- education-num <= 14.5
L   R   L   L   R   R   L   R   L   L   |- INCOME >50k
L   R   L   L   R   R   L   R   L   R   |- INCOME >50k
L   R   L   L   R   R   L   R   R   |- occupation is Other-service
L   R   L   L   R   R   L   R   R   L   |- INCOME <=50k
L   R   L   L   R   R   L   R   R   R   |- INCOME >50k
L   R   L   L   R   R   R   |- capital-gain <= 4225.0
L   R   L   L   R   R   R   L   |- INCOME <=50k
L   R   L   L   R   R   R   R   |- capital-gain <= 4447.0
L   R   L   L   R   R   R   R   L   |- occupation is Exec-managerial
L   R   L   L   R   R   R   R   L   L   |- INCOME >50k
L   R   L   L   R   R   R   R   L   R   |- INCOME >50k
L   R   L   L   R   R   R   R   R   |- INCOME <=50k
L   R   L   R   |- capital-loss <= 1989.5
L   R   L   R   L   |- age <= 28.5
L   R   L   R   L   L   |- workclass is Local-gov
L   R   L   R   L   L   L   |- INCOME <=50k
L   R   L   R   L   L   R   |- INCOME >50k
L   R   L   R   L   R   |- workclass is Federal-gov
L   R   L   R   L   R   L   |- age <= 48.5
L   R   L   R   L   R   L   L   |- INCOME >50k
L   R   L   R   L   R   L   R   |- INCOME <=50k
L   R   L   R   L   R   R   |- INCOME >50k
L   R   L   R   R   |- capital-loss <= 2115.5
L   R   L   R   R   L   |- INCOME <=50k
L   R   L   R   R   R   |- workclass is Local-gov
L   R   L   R   R   R   L   |- INCOME <=50k
L   R   L   R   R   R   R   |- INCOME >50k
L   R   R   |- age <= 84.5
L   R   R   L   |- occupation is Farming-fishing
L   R   R   L   L   |- INCOME >50k
L   R   R   L   R   |- INCOME >50k
L   R   R   R   |- INCOME >50k
R   |- capital-gain <= 7073.5
R   L   |- education-num <= 12.5
R   L   L   |- capital-loss <= 2218.5
R   L   L   L   |- hours-per-week <= 40.5
R   L   L   L   L   |- age <= 32.5
R   L   L   L   L   L   |- martial-status is Married-AF-spouse
R   L   L   L   L   L   L   |- INCOME <=50k
R   L   L   L   L   L   R   |- fnlwgt <= 23759.0
R   L   L   L   L   L   R   L   |- fnlwgt <= 23381.0
R   L   L   L   L   L   R   L   L   |- INCOME <=50k
R   L   L   L   L   L   R   L   R   |- INCOME >50k
R   L   L   L   L   L   R   R   |- occupation is Protective-serv
R   L   L   L   L   L   R   R   L   |- fnlwgt <= 425858.0
R   L   L   L   L   L   R   R   R   |- martial-status is Widowed
R   L   L   L   L   R   |- occupation is Prof-specialty
R   L   L   L   L   R   L   |- sex is Male
R   L   L   L   L   R   L   L   |- capital-gain <= 4718.5
R   L   L   L   L   R   L   L   L   |- fnlwgt <= 29452.0
R   L   L   L   L   R   L   L   L   L   |- INCOME >50k
R   L   L   L   L   R   L   L   L   R   |- INCOME <=50k
R   L   L   L   L   R   L   L   R   |- INCOME >50k
R   L   L   L   L   R   L   R   |- workclass is Federal-gov
R   L   L   L   L   R   L   R   L   |- education is Assoc-acdm
R   L   L   L   L   R   L   R   L   L   |- INCOME >50k
R   L   L   L   L   R   L   R   L   R   |- INCOME <=50k
R   L   L   L   L   R   L   R   R   |- capital-loss <= 1472.0
R   L   L   L   L   R   R   |- occupation is Exec-managerial
R   L   L   L   L   R   R   L   |- capital-gain <= 5373.5
R   L   L   L   L   R   R   L   L   |- fnlwgt <= 186475.5
R   L   L   L   L   R   R   L   R   |- INCOME >50k
R   L   L   L   L   R   R   R   |- martial-status is Married-AF-spouse
R   L   L   L   L   R   R   R   L   |- INCOME <=50k
R   L   L   L   L   R   R   R   R   |- capital-gain <= 4718.5
R   L   L   L   R   |- age <= 38.5
R   L   L   L   R   L   |- workclass is Private
R   L   L   L   R   L   L   |- education-num <= 10.5
R   L   L   L   R   L   L   L   |- relationship is Not-in-family
R   L   L   L   R   L   L   L   L   |- fnlwgt <= 30808.5
R   L   L   L   R   L   L   L   R   |- hours-per-week <= 98.5
R   L   L   L   R   L   L   R   |- martial-status is Married-AF-spouse
R   L   L   L   R   L   L   R   L   |- INCOME >50k
R   L   L   L   R   L   L   R   R   |- capital-gain <= 3692.0
R   L   L   L   R   L   L   R   R   L   |- INCOME <=50k
R   L   L   L   R   L   L   R   R   R   |- INCOME >50k
R   L   L   L   R   L   R   |- education is 12th
R   L   L   L   R   L   R   L   |- INCOME >50k
R   L   L   L   R   L   R   R   |- fnlwgt <= 341657.5
R   L   L   L   R   L   R   R   L   |- occupation is Exec-managerial
R   L   L   L   R   L   R   R   R   |- race is Asian-Pac-Islander
R   L   L   L   R   L   R   R   R   L   |- INCOME >50k
R   L   L   L   R   L   R   R   R   R   |- INCOME <=50k
R   L   L   L   R   R   |- sex is Male
R   L   L   L   R   R   L   |- education is Some-college
R   L   L   L   R   R   L   L   |- fnlwgt <= 351663.0
R   L   L   L   R   R   L   L   L   |- capital-gain <= 4601.5
R   L   L   L   R   R   L   L   L   L   |- INCOME <=50k
R   L   L   L   R   R   L   L   L   R   |- INCOME >50k
R   L   L   L   R   R   L   L   R   |- workclass is Private
R   L   L   L   R   R   L   L   R   L   |- INCOME <=50k
R   L   L   L   R   R   L   L   R   R   |- INCOME >50k
R   L   L   L   R   R   L   R   |- age <= 52.5
R   L   L   L   R   R   L   R   L   |- fnlwgt <= 21613.5
R   L   L   L   R   R   L   R   L   L   |- INCOME >50k
R   L   L   L   R   R   L   R   L   R   |- INCOME <=50k
R   L   L   L   R   R   L   R   R   |- relationship is Not-in-family
R   L   L   L   R   R   R   |- martial-status is Married-AF-spouse
R   L   L   L   R   R   R   L   |- INCOME >50k
R   L   L   L   R   R   R   R   |- occupation is Tech-support
R   L   L   L   R   R   R   R   L   |- martial-status is Divorced
R   L   L   L   R   R   R   R   L   L   |- INCOME <=50k
R   L   L   L   R   R   R   R   L   R   |- INCOME >50k
R   L   L   L   R   R   R   R   R   |- occupation is Protective-serv
R   L   L   R   |- fnlwgt <= 125450.5
R   L   L   R   L   |- occupation is Sales
R   L   L   R   L   L   |- INCOME <=50k
R   L   L   R   L   R   |- age <= 60.0
R   L   L   R   L   R   L   |- INCOME >50k
R   L   L   R   L   R   R   |- INCOME <=50k
R   L   L   R   R   |- capital-loss <= 2391.5
R   L   L   R   R   L   |- education is Assoc-acdm
R   L   L   R   R   L   L   |- INCOME >50k
R   L   L   R   R   L   R   |- age <= 37.5
R   L   L   R   R   L   R   L   |- INCOME <=50k
R   L   L   R   R   L   R   R   |- capital-loss <= 2298.5
R   L   L   R   R   L   R   R   L   |- INCOME >50k
R   L   L   R   R   L   R   R   R   |- INCOME <=50k
R   L   L   R   R   R   |- capital-loss <= 3253.5
R   L   L   R   R   R   L   |- INCOME >50k
R   L   L   R   R   R   R   |- INCOME <=50k
R   L   R   |- hours-per-week <= 43.5
R   L   R   L   |- age <= 33.5
R   L   R   L   L   |- martial-status is Married-AF-spouse
R   L   R   L   L   L   |- INCOME >50k
R   L   R   L   L   R   |- capital-loss <= 2116.0
R   L   R   L   L   R   L   |- age <= 29.5
R   L   R   L   L   R   L   L   |- martial-status is Separated
R   L   R   L   L   R   L   L   L   |- INCOME <=50k
R   L   R   L   L   R   L   L   R   |- fnlwgt <= 41173.5
R   L   R   L   L   R   L   R   |- sex is Male
R   L   R   L   L   R   L   R   L   |- education-num <= 14.5
R   L   R   L   L   R   L   R   R   |- occupation is Tech-support
R   L   R   L   L   R   R   |- INCOME <=50k
R   L   R   L   R   |- education-num <= 14.5
R   L   R   L   R   L   |- capital-loss <= 2232.0
R   L   R   L   R   L   L   |- capital-gain <= 4668.5
R   L   R   L   R   L   L   L   |- age <= 46.5
R   L   R   L   R   L   L   L   L   |- fnlwgt <= 126688.0
R   L   R   L   R   L   L   L   R   |- hours-per-week <= 31.0
R   L   R   L   R   L   L   R   |- capital-gain <= 5194.5
R   L   R   L   R   L   L   R   L   |- INCOME >50k
R   L   R   L   R   L   L   R   R   |- INCOME <=50k
R   L   R   L   R   L   R   |- workclass is Private
R   L   R   L   R   L   R   L   |- INCOME >50k
R   L   R   L   R   L   R   R   |- INCOME <=50k
R   L   R   L   R   R   |- sex is Male
R   L   R   L   R   R   L   |- martial-status is Divorced
R   L   R   L   R   R   L   L   |- INCOME <=50k
R   L   R   L   R   R   L   R   |- fnlwgt <= 93895.5
R   L   R   L   R   R   L   R   L   |- INCOME <=50k
R   L   R   L   R   R   L   R   R   |- workclass is Local-gov
R   L   R   L   R   R   L   R   R   L   |- INCOME <=50k
R   L   R   L   R   R   L   R   R   R   |- INCOME >50k
R   L   R   L   R   R   R   |- workclass is State-gov
R   L   R   L   R   R   R   L   |- education is Doctorate
R   L   R   L   R   R   R   L   L   |- INCOME >50k
R   L   R   L   R   R   R   L   R   |- INCOME <=50k
R   L   R   L   R   R   R   R   |- workclass is Federal-gov
R   L   R   L   R   R   R   R   L   |- INCOME >50k
R   L   R   L   R   R   R   R   R   |- occupation is Machine-op-inspct
R   L   R   L   R   R   R   R   R   L   |- INCOME >50k
R   L   R   L   R   R   R   R   R   R   |- INCOME <=50k
R   L   R   R   |- age <= 27.5
R   L   R   R   L   |- capital-loss <= 2116.0
R   L   R   R   L   L   |- hours-per-week <= 62.5
R   L   R   R   L   L   L   |- workclass is Self-emp-inc
R   L   R   R   L   L   L   L   |- INCOME <=50k
R   L   R   R   L   L   L   R   |- occupation is Craft-repair
R   L   R   R   L   L   L   R   L   |- INCOME <=50k
R   L   R   R   L   L   L   R   R   |- hours-per-week <= 53.5
R   L   R   R   L   L   R   |- fnlwgt <= 78354.0
R   L   R   R   L   L   R   L   |- INCOME >50k
R   L   R   R   L   L   R   R   |- occupation is Sales
R   L   R   R   L   L   R   R   L   |- INCOME <=50k
R   L   R   R   L   L   R   R   R   |- occupation is Exec-managerial
R   L   R   R   L   R   |- INCOME <=50k
R   L   R   R   R   |- capital-loss <= 2391.5
R   L   R   R   R   L   |- occupation is Exec-managerial
R   L   R   R   R   L   L   |- age <= 39.5
R   L   R   R   R   L   L   L   |- fnlwgt <= 185983.5
R   L   R   R   R   L   L   L   L   |- martial-status is Divorced
R   L   R   R   R   L   L   L   L   L   |- INCOME >50k
R   L   R   R   R   L   L   L   L   R   |- INCOME <=50k
R   L   R   R   R   L   L   L   R   |- fnlwgt <= 572687.5
R   L   R   R   R   L   L   L   R   L   |- INCOME <=50k
R   L   R   R   R   L   L   L   R   R   |- INCOME >50k
R   L   R   R   R   L   L   R   |- workclass is Self-emp-not-inc
R   L   R   R   R   L   L   R   L   |- education is Bachelors
R   L   R   R   R   L   L   R   L   L   |- INCOME <=50k
R   L   R   R   R   L   L   R   L   R   |- INCOME >50k
R   L   R   R   R   L   L   R   R   |- education-num <= 14.5
R   L   R   R   R   L   L   R   R   L   |- INCOME >50k
R   L   R   R   R   L   L   R   R   R   |- INCOME >50k
R   L   R   R   R   L   R   |- education-num <= 14.5
R   L   R   R   R   L   R   L   |- sex is Male
R   L   R   R   R   L   R   L   L   |- martial-status is Divorced
R   L   R   R   R   L   R   L   R   |- fnlwgt <= 154245.5
R   L   R   R   R   L   R   R   |- age <= 32.5
R   L   R   R   R   L   R   R   L   |- fnlwgt <= 401751.5
R   L   R   R   R   L   R   R   L   L   |- INCOME <=50k
R   L   R   R   R   L   R   R   L   R   |- INCOME >50k
R   L   R   R   R   L   R   R   R   |- fnlwgt <= 40537.5
R   L   R   R   R   L   R   R   R   L   |- INCOME <=50k
R   L   R   R   R   L   R   R   R   R   |- INCOME >50k
R   L   R   R   R   R   |- INCOME >50k
R   R   |- age <= 20.0
R   R   L   |- INCOME <=50k
R   R   R   |- capital-gain <= 8296.0
R   R   R   L   |- education-num <= 11.5
R   R   R   L   L   |- INCOME <=50k
R   R   R   L   R   |- INCOME >50k
R   R   R   R   |- capital-gain <= 30961.5
R   R   R   R   L   |- INCOME >50k
R   R   R   R   R   |- capital-gain <= 67047.0
R   R   R   R   R   L   |- INCOME <=50k
R   R   R   R   R   R   |- INCOME >50k

```

At Last, we print the prediction result of evaluation on Evaluation SET

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
