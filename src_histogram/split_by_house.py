"""
    Returns the values splitted by houses for numerical headers
"""
def split_by_house(headers, data):
    values_by_houses = {house: {head: [] for head in headers} for house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]}
    for i in range(len(data["Hogwarts House"]) - 1):
        missing = False
        for head in headers:
            if (data[head][i]) == "":
                missing = True
        for head in headers:
            if missing == False:
                values_by_houses[data["Hogwarts House"][i]][head].append(data[head][i])
    return(values_by_houses)