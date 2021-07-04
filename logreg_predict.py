import sys
from src_describe.read_data import read_data
from src_describe.get_values import get_values
from src_logreg_predict.read_coeff import read_coeff
from src_logreg_predict.data_cleaning import data_cleaning
from src_logreg_predict.predict_house import predict_house
from src_logreg_predict.data_normalization import data_normalization

"""
    GOAL: Take data and predict the Houses.
    1.  Read the data
    2.  Clean and normalize the data
    3.  Predict the values
    4.  Print the predictions in houses.csv
"""
if __name__ == '__main__':
    if (len(sys.argv) > 2 and sys.argv[1].lower().endswith('.csv')):
        try:
            data = read_data(sys.argv[1])
            weights_dict = read_coeff(sys.argv[2])
            if (data):
                if (weights_dict):
                    data_cleaning(data)
                    headers = data.pop(0)
                    headers.pop(2)
                    headers.pop(2)
                    data_normalization(data, headers)
                    predict_house(data, weights_dict)
                else:
                    print("Coefficients are invalid")
            else:
                print('\033[93m'+"Please provide the path of the dataset and the weights of the features as arguments")
        except ValueError:
            print('\033[93m'+"Please provide the path of the dataset and the weights of the features as arguments")
    else:
        print('\033[93m'+"Please provide the path of the dataset and the weights of the features as arguments")