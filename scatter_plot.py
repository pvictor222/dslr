import sys
from src_describe.read_data import read_data
from src_describe.get_values import get_values
from src_histogram.split_by_house import split_by_house
from src_scatter_plot.calc_pearson_cor import calc_pearson_cor
from src_scatter_plot.print_scatter_plot import print_scatter_plot
from src_scatter_plot.remove_missing_rows import remove_missing_rows

"""

"""
if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1].lower().endswith('.csv')):
        try:
            data = read_data(sys.argv[1])
            if (data):
                headers = data.pop(0)
                values_dict = get_values(headers, data)
                values_dict = remove_missing_rows(values_dict)
                print(values_dict)
                pearson_cor = calc_pearson_cor(values_dict)
                values_by_house = split_by_house(headers, values_dict)
                print_scatter_plot(values_by_house)
            else:
                print("Please provide the path of the dataset as an argument")
        except ValueError:
            print(ValueError) # to delete
            print("Please provide the path of the dataset as an argument")
    else:
        print("Please provide the path of the dataset as an argument")