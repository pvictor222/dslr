# dslr - Datascience X Logistic Regression (42 School Project)

*Project done by @pvictor using Julia language*

## 1. Data Analysis
### Program: "describe.jl"
**Goal:** Read the dataset and calculate the mean, standard deviation, max, min, and quartiles for all numerical features.
**Bonus:** 
1. Number of missing elements for each
2. Description of the non-numerical values
3. Pretty formating

## 2. Data Visualization
### Program: "histogram.jl"
**Goal:** Create a histogram the repartition of grades among the houses for each course
### Program: "scatter_plot.jl"
**Goal:** Create a scatter plot of the features
### Program: "pair_plot.jl"
**Goal:** Create a pair plot to determine which features to use for the logistic regression

## 3. Logistic Regression
### Program: "logreg_train.jl"
**Goal:** Read the training dataset and train a logistic regression using gradient descent and store the weights of the features in "predict.txt"
### Program: "logreg_predict.jl"
**Goal:** Read the testing dataset and output predictions based on the weights calculated by "logreg_train.jl"
**Bonus:** "precision.jl" to evaluate the precision of the predictions made in "logreg_predict.jl"