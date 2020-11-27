import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from src_histogram.get_num_headers import get_num_headers

def print_histogram(values):
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
    color_table = {"Gryffindor": "red", "Ravenclaw": "blue", "Hufflepuff": "gold", "Slytherin": "green"}
    for head in num_headers:
        for house in ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            temp_trace = go.Histogram(x=values[house][head],
                                        nbinsx=20,
                                        marker = dict(color=color_table[house]),
                                        name=house,
                                        legendgroup=head)
            fig.append_trace(temp_trace, i, j)
        j += 1
        if j > nb_columns:
            j = 1
            i += 1
    fig.update_layout(
        title="Repartition of grades by Hogwarts Houses"
    )
    fig.update_traces(opacity=0.75)
    fig.show()