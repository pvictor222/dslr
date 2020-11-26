# import sources
import sys
from src_describe.read_data import read_data
from src_describe.get_values import get_values
from src_describe.calc_description import calc_description
from src_describe.print_tables import print_tables

"""
    1. Read the data
    2. Separate numerical headers from non-numerical headers 
    3. Do the calculations
    4. Print using plotly
"""
if __name__ == '__main__':
    if (len(sys.argv) > 1):
        data = read_data(sys.argv[1])
        if (data):
            headers = data.pop(0)
            values_dict = get_values(headers, data)
            describe_dict = calc_description(headers, values_dict)
            print_tables(describe_dict)
    else:
        print("Please provide the path of the dataset as an argument")