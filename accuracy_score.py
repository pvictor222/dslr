import sys
from src_describe.read_data import read_data
import numpy as np
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    if (len(sys.argv) > 2 and sys.argv[1].lower().endswith('.csv') and sys.argv[2].lower().endswith('.csv')):
        try:
            y_pred = [elem[1] for elem in read_data(sys.argv[1])[1:]]
            y_true = [elem[1] for elem in read_data(sys.argv[2])[1:]]
            if (y_pred and y_true):
                if (len(y_pred) == len(y_true)):
                    accuracy = accuracy_score(y_true, y_pred)
                    print("The accuracy of the predictions is: " + str(round(accuracy * 100)) + "%")
                else:
                    print("The numbers of values are different")
            else:
                print("Values are invalid 1")
        except:
            print("Values are invalid 2")
    else:
        print("Please provide the path of the predictions and the real values")
