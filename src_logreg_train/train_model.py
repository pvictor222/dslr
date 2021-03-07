import random # used for mock values ==> to delete
import numpy as np

"""
    Multinomial Logistic Regression
    https://towardsdatascience.com/ml-from-scratch-multinomial-logistic-regression-6dda9cbacf9d
    - Mock values for prediction testing
    -   De-normalize the coefficients
    -   Printing the values
"""

def loss(h, y):
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

def sigmoid(z):
    return (1 / (1 + np.exp(-z)))

def train_model(data, headers):
    
    
    # z = np.dot(X, theta)
    # h = sigmoid(z)
    # gradient = np.dot(X.T, (h - y)) / y.shape[0]
    # lr = 0.01
    # theta -= lr * gradient

    coeffs = {head: random.randrange(1, 10) for head in headers}
    coeff_keys = list(coeffs.keys())
    print(coeff_keys)
    print(sigmoid(2))


    # 1/ Define the target and features arrays
    target = [elem[1] for elem in data]
    features = [[elem[0], elem[2], elem[3],
                elem[4], elem[5], elem[6],
                elem[7], elem[8], elem[9],
                elem[10], elem[11], elem[12],
                elem[13], elem[14], elem[15],
                elem[16], elem[17], elem[18],
                elem[19]] for elem in data]

    # 2/
    # 3/
    # 4/
    # 5/
    # 6/
    # 7/ Print weights

    # De-normalize the coefficients (todo)

    f = open("coeffs.csv", "w")
    f.write(coeff_keys[0] + ":" + str(coeffs[coeff_keys[0]]) + "\n")
    f.close()
    for coeff in coeff_keys[1:]:
        f = open("coeffs.csv", "a")
        f.write(coeff + ":" + str(coeffs[coeff]) + "\n")
        f.close()