import numpy as np

def sigmoid(z):
    # print(-z)
    # print(np.exp(-z))
    return 1 / (1 + np.exp(-z))