import math
"""

https://www.geeksforgeeks.org/implementation-of-logistic-regression-from-scratch-using-python/
https://www.geeksforgeeks.org/understanding-logistic-regression/

    Logistic function (or sigmoid function)
    g(z) = 1 / (1 + e^(-z))

"""

def hypothesis(coeff, data):
    print("in Hypothesis")
    keys = coeff.keys()
    X = [coeff[key] for key in keys]
    print(X)
    # calculate z
    #z = np.dot(X, coeffs)
    z = 2
    g = (1 / (1 + math.exp(-z)))
    print(g)