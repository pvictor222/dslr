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
        temp.pop()
        print(temp)
        temp = temp[0].split(";")
        data = [x.split(':') for x in temp]
        print(data)
        coeff = {elem[0]: elem[1] for elem in data}
        return (coeff)
    else:
        print("Error while reading the coeff file")
        return (False)