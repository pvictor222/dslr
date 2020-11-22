"""
    Goal: Put all the values in a dictionnary organized by headers
"""

def get_values(headers, data):
    values_dict = {head: [] for head in headers}
    for head in headers:
        for elem in data:
            if elem != ['']:
                temp1 = headers.index(head)
                temp2 = elem[temp1]
                values_dict[head].append(temp2)
    return(values_dict)