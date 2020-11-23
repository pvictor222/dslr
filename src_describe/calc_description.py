from src_describe.count_values import count_values, count_missing_values
from src_describe.remove_missing import remove_missing
from src_describe.sum_values import sum_values
from src_describe.standard_deviation import standard_deviation
from src_describe.min_values import min_values
from src_describe.quartiles import q1_value
from src_describe.quartiles import q2_value
from src_describe.quartiles import q3_value
from src_describe.max_values import max_values

"""
    Goal: calculate all the description values
    - For numerical values:
        - Count
        - Number of missing values
        - Mean
        - Standard deviation
        - Min
        - Q1
        - Q2
        - Q3
        - Max
    - For non-numerical values:
        - Count
        - Number of missing values
        - Number of different values
        - Average occurence of a value
        - Most common value
        - Most common value occurences
"""

def calc_description(headers, values_dict):
    describe_dict_num = {head: [] for head in headers}
    describe_dict_non_num = {head: [] for head in headers}
    missing_values = {head: count_missing_values(values_dict[head]) for head in headers}
    remove_missing(headers, values_dict)
    for head in headers:
        try:
            (float(values_dict[head][1]) or int(values_dict[head][1]))
            describe_dict_non_num.pop(head)
            describe_dict_num[head].append(count_values(values_dict[head]))
            describe_dict_num[head].append(missing_values[head])
            values_sum = sum_values(values_dict[head])
            describe_dict_num[head].append(round(values_sum/describe_dict_num[head][0], 2))
            describe_dict_num[head].append(standard_deviation(values_dict[head], describe_dict_num[head][2], describe_dict_num[head][0]))
            describe_dict_num[head].append(min_values(values_dict[head]))
            describe_dict_num[head].append(q1_value(values_dict[head]))
            describe_dict_num[head].append(q2_value(values_dict[head]))
            describe_dict_num[head].append(q3_value(values_dict[head]))
            describe_dict_num[head].append(max_values(values_dict[head]))
        except ValueError:
            describe_dict_num.pop(head)
            describe_dict_non_num[head].append(count_values(values_dict[head]))
            describe_dict_non_num[head].append(missing_values[head])
    return (describe_dict_num, describe_dict_non_num)