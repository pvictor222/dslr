import sys
from src_describe.read_data import read_data
from src_describe.get_values import get_values
# from src_histogram.split_by_house import split_by_house
from src_pair_plot.print_pair_plot import print_pair_plot
from src_scatter_plot.remove_missing_rows import remove_missing_rows
from src_scatter_plot.remove_non_num import remove_non_num

"""
    GOAL: 
"""
if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1].lower().endswith('.csv')):
        try:
            data = read_data(sys.argv[1])
            if (data):
                headers = data.pop(0)
                values_dict = get_values(headers, data)
                values_dict = remove_missing_rows(values_dict)
                # values_by_house = split_by_house(headers, values_dict)
                # values_dict = {house: remove_non_num(values_by_house[house]) for house in values_by_house}
                values_dict = remove_non_num(values_dict)
                print_pair_plot(values_dict)
            else:
                print("Please provide the path of the dataset as an argument")
        except ValueError:
            print(ValueError)
            print("Please provide the path of the dataset as an argument")
    else:
        print("Please provide the path of the dataset as an argument")