# DSLR - Datascience X Logistic Regression (42 School Project)

*Project done by @pvictor using Python*

## 1. Data Analysis
### DESCRIBE.PY
**Show the main characteristics of the data**
1. Read the data
2. Separate numerical headers from non-numerical headers 
3. Do the calculations
4. Print using plotly

## 2. Data Visualization
### HISTOGRAM.PY
**Print histograms of all features with numerical data (except "Index") for each House:**
1. Get the values
2. Split them by houses
3. Print the histogram
**"Arithmancy" and "Care of Magical Creatures" have a similar shape around all four houses**

### SCATTER_PLOT.PY
**Find the 2 features with the stronger relationship and print the scatter plot.**
1. Read the data and organize it by subject
2. Remove missing rows
3. Calculate the Pearson correlations for all couple of subjects and find the one with the stronger relationship
4. Print the result on the terminal
5. Print the scatter plot
**"Defense Against the Dark Arts" and "Astronomy" are similar features**

### PAIR_PLOT.PY
**Print the pair plot or scatter matrix of the features**

## 3. Logistic Regression
### LOGREG_TRAIN.PY
**Multinomial Logistic Regression with gradient descent**
-   One vs rest strategy : https://en.wikipedia.org/wiki/Multiclass_classification#One-vs.-rest :
    Replace the "House" parameter by 4 parameters, one for each house, with values 1 or 0
-   Cost function: using the cross enthropy cost function (~ similar to mean squared error)
0.  Read the data
1.  Clean the data:
    -   Removing First and Last names
    -   Replace Best Hand by 0/1 values
    -   Split date of birth in 3 variables: Day, Month and Year
2.  Normalize the data: 
    -   Replace missing values by mean value
    -   Min-max normalization
3.  Training:
    -   Gradient descent with One-vs-rest strategy
    -   De-normalize the coefficients
    -   Print the coefficients
### LOGREG_PREDICT.PY
**Output the predictions**
1.  Read the data
2.  Clean and normalize the data
3.  Predict
4.  Print the predictions in houses.csv

### ACCURACY.PY
**Calculates the accuracy of the predictions using Scikit-Learn's accuracy score and outputs whether it's higher or lower than 98%**

### BONUS
1.  Describe:
    - Missing values
    - Description of the non-numerical values
2.  Train: Print the graph of the cost function (if the user wants)
3.  Accuracy.py