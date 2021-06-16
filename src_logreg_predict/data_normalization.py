from src_describe.get_values import get_values
from src_describe.calc_description import calc_description
from src_describe.print_tables import print_tables
from src_logreg_predict.compile_describe_num import compile_describe_num
from src_logreg_predict.min_max_normalization import min_max_normalization

"""
    1.  Getting the min and max values of every header
    2.  Perform min-max normalization on the data 
"""

def data_normalization(data, headers):
    values_dict = get_values(headers, data)
    describe_dict = calc_description(headers, values_dict)
    min_max_dict = compile_describe_num(describe_dict)
    min_max_normalization(min_max_dict, data)
    return min_max_dict