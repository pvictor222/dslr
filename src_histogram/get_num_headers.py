"""
    Return a list of the numerical headers
"""
def get_num_headers(values):
    num_headers = []
    non_num_headers = []
    for elem in values:
        try:
            (float(values[elem][1]) or int(values[elem][1]))
            num_headers.append(elem)
        except:
            non_num_headers.append(elem)
    num_headers.pop(0)
    return (num_headers)