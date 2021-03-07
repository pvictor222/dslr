"""
    Min-max normalization
        If empty: normalized_value = (value - min) / (max - min)
        Else: normalized_value = (mean - min) / (max - min)

"""
def min_max_normalization(describe_dict, data):
    headers = list(describe_dict.keys())
    for line in data:
        for elem in range(0, len(line[3:])):
            if (line[elem + 3] != ''):
                line[elem + 3] = (float(line[elem + 3]) - describe_dict[headers[elem]]["min"]) / (describe_dict[headers[elem]]["max"] - describe_dict[headers[elem]]["min"])
            else:
                line[elem + 3] = (describe_dict[headers[elem]]["mean"] - describe_dict[headers[elem]]["min"]) / (describe_dict[headers[elem]]["max"] - describe_dict[headers[elem]]["min"])