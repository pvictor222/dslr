from src_histogram.get_num_headers import get_num_headers

"""
    GOAL: Remove the non_numerical columns
"""
def remove_non_num(values):
    num_headers = get_num_headers(values)
    num_headers.append("Best Hand")
    num_headers.append("Hogwarts House")
    temp = {head: values[head] for head in num_headers}
    return(temp)