# import sources
from src_describe.read_data import read_data

if __name__ == '__main__':
    data = read_data("datasets/dataset_train.csv")
    if (data):
        print(data[0])
        