import numpy as np
from src_logreg_train.sigmoid import sigmoid
from matplotlib import pyplot as plt

"""
    Multinomial Logistic Regression with gradient descent
    -   https://teddykoker.com/2019/06/multi-class-classification-with-logistic-regression-in-python/
        -   One vs rest strategy : https://en.wikipedia.org/wiki/Multiclass_classification#One-vs.-rest :
            Replace the "House" parameter by 4 parameters, one for each house, with values 1 or 0
        -   Cost function: using the cross enthropy cost function (~ similar to mean squared error)
"""

def cost(theta, x, y):
    """
        Cost = cross enthropy cost function
        Returns costs and gradient
    """
    h = sigmoid(np.dot(x, theta))
    m = len(y)
    cost = 1 / m * np.sum(
        -y * np.log(h) - (1 - y) * np.log(1 - h)
    )
    grad = 1 / m * (np.dot((y - h), x))
    return cost, grad

def fit(x, y, max_iter=1000, alpha=0.5):
    """
        1.  Preparing the variables
            a.  Insert a column in the x matrix (filled with '1')
            b.  houses = A list of all the possible values of y
            c.  thetas = A list which will contain the weights (initialized empty)
            d.  costs = A list which fill contain the costs of all the iterations (initialized with zeros)
            e.  y becomes a np array
        2.  For each house in houses: 
                -   binary_y = 1 if it is the house, 0 otherwise
                -   theta = the list of weights for class (initialized at 0)
                For each iteration:
                    -   Calculate the cost and gradient
                    -   Update theta
                -   Add theta to thetas
        --> Return thetas, houses and costs

    """
    x = np.insert(x, 0, 1, axis=1)
    houses = np.unique(y)
    thetas = []
    costs = np.zeros(max_iter)
    y = np.array(y)
    
    for house in houses:
        binary_y = np.where(y == house, 1, 0)
        theta = np.zeros(x.shape[1])
        for i in range(max_iter):
            costs[i], grad = cost(theta, np.array(x), binary_y)
            theta += alpha * grad
        thetas.append(theta)
        print(costs[i])
    return thetas, houses, costs

def train_model(data, headers):
    """
        1.  y = House parameter
        2.  x = data without the Index, Birthday and House parameters
        3.  Call the fit function to get thetas, houses and costs
        4.  Outputs the weights determined in the fit function
    """
    y = [elem[1] for elem in data]
    x = data
    for elem in x:
        elem.pop(0)
        elem.pop(0)
        elem.pop(0)
    thetas, houses, costs = fit(x, y)
    f = open("coeffs", "w")
    for house in houses:
        f.write(house)
        f.write(";")
    f.close()
    f = open("coeffs", "a")
    for theta in thetas:
        f.write('\n')
        for i in theta:
            f.write(str(i))
            f.write(";")
    plt.plot(costs)
    plt.title("Costs function")
    plt.ylabel("Cost")
    plt.xlabel("Number of iterations")
    plt.show()
    f.close()
