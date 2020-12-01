from src_describe.standard_deviation import standard_deviation
from src_describe.sum_values import sum_values
from src_describe.count_values import count_values
from src_histogram.get_num_headers import get_num_headers
from src_scatter_plot.calc_cov import calc_cov
"""
    GOAL: return a table of all Pearson correlations between the variables
    For all couples of subjects x and y where x != y:
        r = cov(X, Y) / (ecart_type(X) * (ecart_type(Y))
"""
def calc_pearson_cor(values):
    num_headers = get_num_headers(values)
    pearson_cor = {head: {elem: 0 for elem in num_headers} for head in num_headers}
    for h1 in num_headers:
        for h2 in num_headers:
            if h1 == h2:
                pearson_cor[h1][h2] = 0
            else:
                cov = calc_cov(values[h1], values[h2])
                std_1 = standard_deviation(values[h1], sum_values(values[h1]) / len(values[h1]), count_values(values[h1]))
                std_2 = standard_deviation(values[h2], sum_values(values[h2]) / len(values[h2]), count_values(values[h2]))
                pearson_cor[h1][h2] = cov / (std_1 * std_2)
    return (pearson_cor)