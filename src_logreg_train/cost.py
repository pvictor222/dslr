import numpy as np
from src_logreg_train.sigmoid import sigmoid

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