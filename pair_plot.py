import sys
from src_describe.read_data import read_data
from src_describe.get_values import get_values
from src_pair_plot.print_pair_plot import print_pair_plot
from src_scatter_plot.remove_missing_rows import remove_missing_rows
from src_scatter_plot.remove_non_num import remove_non_num

"""
    GOAL: print the pair plot or scatter matrix of the following features:
    - All the numerical features are included, except "Index"
    - Best Hand
"""
if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1].lower().endswith('.csv')):
        try:
            data = read_data(sys.argv[1])
            if (data):
                headers = data.pop(0)
                if "Hogwarts House" in headers:
                    values_dict = get_values(headers, data)
                    if values_dict["Hogwarts House"][0]:
                        values_dict = remove_missing_rows(values_dict)
                        values_dict = remove_non_num(values_dict)
                        print_pair_plot(values_dict)
                    else:
                        print('\033[93m'+"Please provide the path of the dataset with Hogwart Houses")
                else:
                    print('\033[93m'+"Please provide the path of the dataset with Hogwart Houses")
            else:
                print('\033[93m'+"Please provide the path of the dataset as an argument")
        except ValueError:
            print(ValueError)
            print('\033[93m'+"Please provide the path of the dataset as an argument")
    else:
        print('\033[93m'+"Please provide the path of the dataset as an argument")