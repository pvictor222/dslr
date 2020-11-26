from src_describe.count_values import count_values, count_missing_values
from src_describe.remove_missing import remove_missing
from src_describe.sum_values import sum_values
from src_describe.standard_deviation import standard_deviation
from src_describe.min_values import min_values
from src_describe.quartiles import q1_value
from src_describe.quartiles import q2_value
from src_describe.quartiles import q3_value
from src_describe.max_values import max_values
from src_describe.common_values import common_values

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
    describe_dict_num = []
    describe_dict_non_num = []
    missing_values = {head: count_missing_values(values_dict[head]) for head in headers}
    remove_missing(headers, values_dict)
    num_headers = []
    count_num = 0
    count_non_num = 0
    non_num_headers = []
    for head in headers:
        if head != "Index":
            try:
                (float(values_dict[head][1]) or int(values_dict[head][1]))
                describe_dict_num.append([])
                num_headers.append(head)
                describe_dict_num[count_num].append(count_values(values_dict[head]))
                describe_dict_num[count_num].append(missing_values[head])
                values_sum = sum_values(values_dict[head])
                describe_dict_num[count_num].append(round(values_sum/describe_dict_num[count_num][0], 2))
                describe_dict_num[count_num].append(standard_deviation(values_dict[head], describe_dict_num[count_num][2], describe_dict_num[count_num][0]))
                describe_dict_num[count_num].append(min_values(values_dict[head]))
                describe_dict_num[count_num].append(q1_value(values_dict[head]))
                describe_dict_num[count_num].append(q2_value(values_dict[head]))
                describe_dict_num[count_num].append(q3_value(values_dict[head]))
                describe_dict_num[count_num].append(max_values(values_dict[head]))
                count_num += 1
            except ValueError:
                describe_dict_non_num.append([])
                non_num_headers.append(head)
                describe_dict_non_num[count_non_num].append(count_values(values_dict[head]))
                describe_dict_non_num[count_non_num].append(missing_values[head])
                describe_dict_non_num[count_non_num].append(len(set(values_dict[head])))
                describe_dict_non_num[count_non_num].append(round(describe_dict_non_num[count_non_num][0] / describe_dict_non_num[count_non_num][2], 2))
                most_common_values = common_values(values_dict[head])
                describe_dict_non_num[count_non_num].append(most_common_values[0])
                describe_dict_non_num[count_non_num].append(most_common_values[1])
                count_non_num += 1
    describe_dict_num.insert(0, ["Count", "Missing values", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"])
    describe_dict_non_num.insert(0, ["Count", "Missing values", "Number of different values", "Average occurence of a value", "Most common value", "Occurences of the most common value"])
    non_num_headers.insert(0, "Subjects")
    num_headers.insert(0, "Subjects")
    return (describe_dict_num, describe_dict_non_num, num_headers, non_num_headers)