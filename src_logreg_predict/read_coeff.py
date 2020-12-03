import os

"""
    Check if file exists and permissions are ok
    Read the coeff and returns them in a dictionnary
"""
def read_coeff(file):
    if (os.access(file, os.R_OK)):
        try:
            f = open(file, "r")
        except ValueError:
            print("Error while reading the coeff file")
            return (False)
        temp = f.read().split('\n')
        data = [x.split(',') for x in temp]
        data.pop()
        coeff = {elem[0]: elem[1] for elem in data}
        return (coeff)
    else:
        print("Error while reading the coeff file")
        return (False)