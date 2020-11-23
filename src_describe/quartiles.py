"""
    Get the Q1, Q2 and Q3
"""

def q1_value(values):
    values.sort()
    return(round(float(values[int(round(len(values) - 1) / 4)]), 2))

def q2_value(values):
    values.sort()
    return(round(float(values[int(round(len(values) - 1) / 2)]), 2))

def q3_value(values):
    values.sort()
    return(round(float(values[int(round(len(values) - 1) * 3 / 4)]), 2))