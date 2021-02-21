import random # used for mock values ==> to delete

"""
    - Mock values for prediction testing
    - Printing the values
"""

def train_model(data, headers):
    coeffs = {head: random.randrange(1, 10) for head in headers}
    coeff_keys = list(coeffs.keys())
    f = open("coeffs.csv", "w")
    f.write(coeff_keys[0] + ":" + str(coeffs[coeff_keys[0]]) + "\n")
    f.close()
    for coeff in coeff_keys[1:]:
        f = open("coeffs.csv", "a")
        f.write(coeff + ":" + str(coeffs[coeff]) + "\n")
        f.close()