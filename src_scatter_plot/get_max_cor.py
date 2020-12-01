"""
    GOAL: Find the two features with the max correlation
    ==> return (feature 1, feature 2, correlation score)
"""
def get_max_cor(cor_table):
    max = 0
    feature_1 = ""
    feature_2 = ""
    for f1 in cor_table:
        for f2 in cor_table[f1]:
            if (f1 != f2 and abs(cor_table[f1][f2]) > abs(max)):
                max = cor_table[f1][f2]
                feature_1 = f1
                feature_2 = f2
    return (max, feature_1, feature_2)