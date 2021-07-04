import numpy as np
from src_logreg_train.cost import cost

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
    return thetas, houses, costs