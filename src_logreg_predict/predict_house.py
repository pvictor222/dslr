import numpy as np
from src_logreg_train.sigmoid import sigmoid
"""

"""

def predict(houses, weights_dict, x):
    """

    """
    thetas = []
    for elem in weights_dict:
        thetas.append(np.array(weights_dict[elem]))
    for line in thetas:
        line = [float(x) for x in line]
    # print(thetas)
    x = np.array(x)
    x = np.insert(x, 0, 1, axis=1)
    # print(thetas)
    predictions = [np.argmax(
        [sigmoid(np.dot(elem, theta)) for theta in thetas]
    ) for elem in x]
    return [houses[pred] for pred in predictions]



def predict_house(data, weights_dict):
    """
        1.  x = data without the Index, Birthday and House parameters
        2.  Call the fit function
        3.  Outputs the weights determined in the fit function
    """
    x = data
    for elem in x:
        elem.pop(0)
        elem.pop(0)
        elem.pop(0)
    houses = list(weights_dict.keys())
    predictions = predict(houses, weights_dict, x)
    print(predictions)
    # thetas, houses, costs = fit(x, y)
    # f = open("coeffs", "w")
    # for house in houses:
    #     f.write(house)
    #     f.write(";")
    # f.close()
    # f = open("coeffs", "a")
    # for theta in thetas:
    #     f.write('\n')
    #     for i in theta:
    #         f.write(str(i))
    #         f.write(";")
    # f.close()