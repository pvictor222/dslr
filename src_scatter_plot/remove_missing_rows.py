from src_histogram.get_num_headers import get_num_headers
"""
    Removes the entire row when one numerical value is missing
"""
def remove_missing_rows(values):
    # num_headers = get_num_headers(values)
    for head in values:
        i = len(values[head]) - 1
        while i >= 0 :
            if (values[head][i] == ""):
                for head in values:
                    values[head].pop(i)
            else:
                i -= 1
    return (values)
