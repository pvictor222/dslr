from src_logreg_train.fit import fit
from matplotlib import pyplot as plt

def train_model(data, headers, bonus):
    """
        1.  y = House parameter
        2.  x = data without the Index, Birthday and House parameters
        3.  Call the fit function to get thetas, houses and costs
        4.  Outputs the weights determined in the fit function
    """
    y = [elem[1] for elem in data]
    x = data
    for elem in x:
        elem.pop(0)
        elem.pop(0)
        elem.pop(0)
    thetas, houses, costs = fit(x, y)
    f = open("coeffs", "w")
    for house in houses:
        f.write(house)
        f.write(";")
    f.close()
    f = open("coeffs", "a")
    for theta in thetas:
        f.write('\n')
        for i in theta:
            f.write(str(i))
            f.write(";")
    f.close()
    if bonus["print_cost_fonction"] == 1:
        plt.plot(costs)
        plt.title("Costs function")
        plt.ylabel("Cost")
        plt.xlabel("Number of iterations")
        plt.show()
