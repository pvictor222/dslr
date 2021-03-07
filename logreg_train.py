import sys
from src_describe.read_data import read_data
from src_describe.get_values import get_values
from src_logreg_predict.read_coeff import read_coeff
from src_logreg_predict.data_cleaning import data_cleaning
from src_logreg_predict.data_normalization import data_normalization
from src_logreg_train.train_model import train_model

"""
    1.  Cleaning the data:
        -   Removing First and Last names
        -   Replace Best Hand by 0/1 values
        -   Split date of birth in 3 variables: Day, Month and Year
    2.  Normalize the data: 
        -   Replace missing values by mean value
        -   Min-max normalization
    3.  Training:
        -
        -   De-normalize the coefficients
        -   Print the coefficients
"""

if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1].lower().endswith('.csv')):
        try:
            data = read_data(sys.argv[1])
            if (data):
                data_cleaning(data)
                headers = data.pop(0)
                headers.pop(2)
                headers.pop(2)
                min_max_dict = data_normalization(data, headers)
                #todo: training
                train_model(data, headers)
            else:
                print("An error has appeared. Please make sure the data in arguments is correct")
        except ValueError:
            print("An error has appeared. Please make sure the data in arguments is correct")
    else:
        print("An error has appeared. Please make sure the data in arguments is correct")