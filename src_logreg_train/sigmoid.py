import numpy as np

"""
    'A sigmoid function is a mathematical function having a characteristic "S"-shaped curve or sigmoid curve.
    A common example of a sigmoid function is the logistic function.'
    (Wikipedia)
"""

def sigmoid(z):
    """
        Returns the logistic function, also called sigmoid function
    """
    return 1 / (1 + np.exp(-z))