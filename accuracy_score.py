import sys
import numpy as np
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    if (len(sys.argv) > 2 and sys.argv[1].lower().endswith('.csv') and sys.argv[2].lower().endswith('.csv')):
        y_pred = [0, 2, 1, 3]
        y_true = [0, 1, 2, 3]
        accuracy = accuracy_score(y_true, y_pred)
        print("The accuracy of the predictions is: " + str(round(accuracy * 100)) + "%")
    else:
        print("Please provide the path of the predictions and the real values")
