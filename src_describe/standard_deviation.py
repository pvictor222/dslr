import math
"""
    Goal: Return the standard deviation of the list
"""

def standard_deviation(data, mean, count):
    variance = 0
    for elem in data:
        variance += (float(elem) - mean) ** 2 
    return round(math.sqrt(variance / (count - 1)), 2)
