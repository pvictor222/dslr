import os

"""
    Check if file exists and permissions are ok
    Read the coeff and returns them in a dictionnary, with the Houses as keys
"""
def read_coeff(file):
    if (os.access(file, os.R_OK)):
        try:
            f = open(file, "r")
        except ValueError:
            print("Error while reading the coeff file")
            return (False)
        temp = f.read().split('\n')
        houses = (temp.pop(0)).split(";")
        houses = list(filter(None, houses))
        data = [list(filter(None, x.split(';'))) for x in temp]
        weights_dict = {house: [] for house in houses}
        i = 0
        for elem in data:
            weights_dict[houses[i]] = elem
            i += 1
        return (weights_dict)
    else:
        print("Error while reading the coeff file")
        return (False)