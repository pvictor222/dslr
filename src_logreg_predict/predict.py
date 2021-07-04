import numpy as np
from src_logreg_train.sigmoid import sigmoid

def predict(houses, weights_dict, x):
    """
        1.  Convert weights and x to np arrays
        2.  Convert to floats
        3.  Predict: for each element in the data:
                - for each house, multiply the features by the coefficients of the house
                - take the maximum output
        4.  Return the house corresponding to the prediction for each element in data
    """
    thetas = []
    for elem in weights_dict:
        thetas.append(np.array(weights_dict[elem]))
    for line in thetas:
        line = [float(x) for x in line]
    x = np.array(x)
    x = np.insert(x, 0, 1, axis=1)
    new_thetas = np.empty([len(thetas), len(thetas[0])], dtype=float)
    for i in range(len(new_thetas)):
        for j in range(len(new_thetas[i])):
            new_thetas[i][j] = float(thetas[i][j])
    predictions = [np.argmax(
                        [sigmoid(np.dot(elem, theta)) for theta in new_thetas]
                    ) for elem in x]
    return [houses[pred] for pred in predictions]