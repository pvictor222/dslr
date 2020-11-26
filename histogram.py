import sys
import plotly.graph_objects as go
from src_describe.read_data import read_data

"""

"""
if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1].lower().endswith('.csv')):
        try:
            data = read_data(sys.argv[1])
            if (data):
                print(data)
            else:
                print("Please provide the path of the dataset as an argument")
        except:
            print("Please provide the path of the dataset as an argument")
    else:
        print("Please provide the path of the dataset as an argument")