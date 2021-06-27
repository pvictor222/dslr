import numpy as np
from src_logreg_train.sigmoid import sigmoid
"""

"""

def predict(houses, weights_dict, x):
    """
        1.  Convert weights and x to np arrays
        2.  Convert to floats
        3.  
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
        for j in range(i):
            new_thetas[i][j] = float(thetas[i][j])
            print("new_thetas["+str(i)+"]["+str(j)+"] = " + str(new_thetas[i][j]))
    print("**** NEW_THETAS ****")
    print(new_thetas)
    predictions = [np.argmax(
        [sigmoid(np.dot(elem, theta)) for theta in new_thetas]
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
    f = open("houses.csv", "w")
    f.write("Index,Hogwarts House")
    for i in range(1, len(predictions)):
        f.write('\n')
        f.write(str(i))
        f.write(',')
        f.write(predictions[i])
    f.close