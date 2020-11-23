"""
    Goal: Returns the max of all the elements
"""

def max_values(values):
    max = float(values[0])
    for value in values:
        if float(value) > max:
            max += float(value)
    return round(max, 2)