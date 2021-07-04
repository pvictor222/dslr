from src_logreg_predict.predict import predict

def predict_house(data, weights_dict):
    """
        1.  x = data without the Index, Birthday and House parameters
        2.  Call the predict function
        3.  Outputs the houses determined in the predict function to "houses.csv"
    """
    x = data
    for elem in x:
        elem.pop(0)
        elem.pop(0)
        elem.pop(0)
    houses = list(weights_dict.keys())
    predictions = predict(houses, weights_dict, x)
    f = open("houses.csv", "w")
    f.write("Index,Hogwarts House\n")
    for i in range(0, len(predictions)):
        f.write(str(i))
        f.write(',')
        f.write(predictions[i])
        f.write('\n')
    f.close