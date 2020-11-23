"""
    Goal: Get the most common value of the list
    Return: (most common value, number of occurences of this value)
"""

def common_values(values):
    values_dict = {elem: 0 for elem in set(values)}
    for value in values:
        values_dict[value] += 1
    most_common = 0
    max = 0
    for elem in set(values):
        if (values_dict[elem] > max):
            max = values_dict[elem]
            most_common = elem
    return (most_common, max)
