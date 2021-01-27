from src_logreg_predict.hypothesis import hypothesis

"""

"""

def predict_house(data, coeff):
    print(coeff)
    print("normalization to do")
    for line in data:
        print(line)
        hypothesis(coeff, line)