from src_describe.get_values import get_values
from src_describe.calc_description import calc_description
from src_describe.print_tables import print_tables
"""

"""

def data_normalization(data, headers):
    values_dict = get_values(headers, data)
    describe_dict = calc_description(headers, values_dict)
    # print(describe_dict)