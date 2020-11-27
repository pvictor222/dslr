from src_describe.sum_values import sum_values
"""
    Returns the covariance of 2 headers
    COV(X,Y) = E[(X - E[X])(Y - E[Y])]
"""
def calc_cov(h1, h2):
    print("ICI")
    print(sum_values(h1))
    moy_h1 = sum_values(h1) / len(h1)
    moy_h2 = sum_values(h2) / len(h2)
    print(moy_h1)