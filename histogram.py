import sys
from src_describe.read_data import read_data
from src_describe.get_values import get_values
from src_histogram.split_by_house import split_by_house
from src_histogram.print_histogram import print_histogram

"""
    Print histograms of all features with numerical data (except "Index") for each House
    1. Get the values
    2. Split them by houses
    3. Print the histogram
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
                        values_by_house = split_by_house(headers, values_dict)
                        print_histogram(values_by_house)
                    else:
                        print('\033[93m'+"Please provide the path of the dataset with Hogwart Houses")
                else:
                    print('\033[93m'+"Please provide the path of the dataset with Hogwart Houses")
            else:
                print('\033[93m'+"Please provide the path of the dataset as an argument")
        except ValueError:
            print('\033[93m'+"Please provide the path of the dataset as an argument")
    else:
        print('\033[93m'+"Please provide the path of the dataset as an argument")