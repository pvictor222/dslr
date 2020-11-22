from src_describe.count_values import count_values
from src_describe.sum_values import sum_values
from src_describe.standard_deviation import standard_deviation

"""
    Goal: calculate all the description values
    - For numerical values:
        - Count
        - Number of missing values
        - Mean
        - Standard deviation
"""

def calc_description(headers, values_dict):
    describe_dict_num = {head: [] for head in headers}
    describe_dict_non_num = {head: [] for head in headers}
    for head in headers:
        try:
            float(values_dict[head][1])
            values_count = count_values(values_dict[head])
            describe_dict_num[head].append(values_count[0])
            describe_dict_num[head].append(values_count[1])
            values_sum = sum_values(values_dict[head])
            describe_dict_num[head].append(values_sum/values_count[0])
            describe_dict_num[head].append(standard_deviation(values_dict[head], values_sum/values_count[0], values_count[0]))
        except ValueError:
            print(head)
    print(describe_dict_num)
    return (describe_dict_num, describe_dict_non_num)