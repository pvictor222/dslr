def calc_sum(values):
    total = 0
    for value in values:
        if value != "":
            total += float(value)
    return (total)

"""
    Returns the covariance of 2 headers
    COV(X,Y) = somme[(X - E[X])(Y - E[Y])] / N
"""
def calc_cov(h1, h2):
    moy_h1 = calc_sum(h1) / len(h1)
    moy_h2 = calc_sum(h2) / len(h2)
    cov = 0
    for i in range(len(h1) - 1):
        if h1[i] != "" and h2[i] != "":
            cov += (float(h1[i]) - moy_h1) * (float(h2[i]) - moy_h2)
    return (cov / len(h1))