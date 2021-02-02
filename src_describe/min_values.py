"""
    Goal: Returns the min of all the elements
"""

def min_values(values):
    min = float(values[0])
    for value in values:
        if float(value) < min:
            min = float(value)
    return round(min, 2)