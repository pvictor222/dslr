"""
    Goal: return a tuple (number of non-empty values, number of missing values)
"""

def count_values(values):
    count = 0
    for elem in values:
        if elem != "":
            count += 1
    return (count)

def count_missing_values(values):
    missing = 0
    for elem in values:
        if elem == "":
            missing += 1
    return (missing)