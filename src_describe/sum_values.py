"""
    Goal: Returns the sum of all the elements
"""

def sum_values(values):
    total = 0
    for value in values:
        if value != "":
            total += float(value)
    return total