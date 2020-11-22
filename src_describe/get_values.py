"""
    Goal: Put all the values in a dictionnary organized by headers
"""

def get_values(headers, data):
    values_dict = {head: [] for head in headers}
    for head in headers:
        for elem in data:
            values_dict[head].append(elem[headers.index(head)])
    return(values_dict)