import sys
from src_describe.read_data import read_data
from src_describe.get_values import get_values
from src_histogram.split_by_house import split_by_house
from src_scatter_plot.calc_pearson_cor import calc_pearson_cor
from src_scatter_plot.print_scatter_plot import print_scatter_plot
from src_scatter_plot.remove_missing_rows import remove_missing_rows
from src_scatter_plot.get_max_cor import get_max_cor

"""
    GOAL: find the 2 features with the stronger relationship and print the scatter plot.
    1. Read the data and organize it by subject
    2. Remove missing rows
    3. Calculate the Pearson correlations for all couple of subjects and find the one with the stronger relationship
    4. Print the result on the terminal
    5. Print the scatter plot
"""
if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1].lower().endswith('.csv')):
        try:
            data = read_data(sys.argv[1])
            if (data):
                headers = data.pop(0)
                values_dict = get_values(headers, data)
                if values_dict["Hogwarts House"][0]:
                    values_dict = remove_missing_rows(values_dict)
                    pearson_cor = calc_pearson_cor(values_dict)
                    max_cor = get_max_cor(pearson_cor)
                    print('\033[94m'+"The most similar features are " + max_cor[1] + " and " + max_cor[2] + " with a pearson correlation of " + str(round(max_cor[0], 2)) + "." )
                    values_by_house = split_by_house(headers, values_dict)
                    print_scatter_plot(values_by_house, max_cor)
                else:
                    print('\033[93m'+"Please provide the path of the dataset with Hogwart Houses")
            else:
                print('\033[93m'+"Please provide the path of the dataset as an argument")
        except ValueError:
            print('\033[93m'+"Please provide the path of the dataset as an argument")
    else:
        print('\033[93m'+"Please provide the path of the dataset as an argument")