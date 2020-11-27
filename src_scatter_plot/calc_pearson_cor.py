from src_histogram.get_num_headers import get_num_headers
from src_scatter_plot.calc_cov import calc_cov
"""
    GOAL: return a table of all Pearson correlations between the variables
    For all couples of subjects x and y where x != y:
        r = cov(X, Y) / (ecart_type(X) * (ecart_type(X))
"""
def calc_pearson_cor(values):
    num_headers = get_num_headers(values)
    person_cor = {head: {elem: -1000 for elem in num_headers} for head in num_headers}
    for h1 in num_headers:
        for h2 in num_headers:
            print(h1)
            print(h2)
            if h1 == h2:
                person_cor[h1][h2] = 1000
            else:
                cov = calc_cov(values[h1], values[h2])
                person_cor[h1][h2] = 0
    print(person_cor)