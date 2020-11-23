"""
    Remove missing values from the dictionary
"""

def remove_missing(headers, values):
    for head in headers:
        i = 0
        while i < len(values[head]):
            if (values[head][i] == ""):
                values[head].pop(i)
                i = 0
            else:
                i += 1
                