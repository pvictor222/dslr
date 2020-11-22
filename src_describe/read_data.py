import os

"""
    Check if file exists and permissions are ok
    Read the data and returns it
"""
def read_data(csv):
    if (os.access(csv, os.R_OK)):
        try:
            f = open(csv, "r")
        except ValueError:
            print("Error while reading the csv file")
            return (False)
        temp = f.read().split('\n')
        data = [x.split(',') for x in temp]
        return (data)
    else:
        print("Error while reading the csv file")
        return (False)