from src_describe.get_values import get_values
from src_describe.calc_description import calc_description
from src_describe.print_tables import print_tables
from src_logreg_predict.compile_describe_num import compile_describe_num
from src_logreg_predict.min_max_normalization import min_max_normalization
"""

"""

def data_normalization(data, headers):
    values_dict = get_values(headers, data)
    describe_dict = calc_description(headers, values_dict)
    describe_dict_num = compile_describe_num(describe_dict)
    normalized_data = min_max_normalization(describe_dict_num, data)
    print(describe_dict_num)