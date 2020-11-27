from src_histogram.get_num_headers import get_num_headers
# import plotly.express as px
import plotly.graph_objects as go
# import sys
from plotly.subplots import make_subplots
"""

"""
def print_scatter_plot(values):
    num_headers = get_num_headers(values["Slytherin"])
    nb_columns = 3
    if len(num_headers) % nb_columns == 0:
        nb_rows = len(num_headers) / nb_columns
    else:
        nb_rows = round(len(num_headers) / nb_columns) + 1
    fig = make_subplots(rows=int(nb_rows),
                        cols=nb_columns,
                        subplot_titles=(num_headers))
    i = 1
    j = 1
    for head in num_headers:
        temp_trace = go.Scatter(x=values["Slytherin"][head],
                                y=values["Slytherin"]["Potions"],
                                mode='markers')   
        fig.append_trace(temp_trace, i, j)
        j += 1
        if j > nb_columns:
            j = 1
            i += 1
    # for head in num_headers:
    #     temp_trace = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    #     fig.append_trace(temp_trace, i, j)
    fig.update_layout(
        title="Grades repartition"
    )
    fig.show()