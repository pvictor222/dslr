import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
from src_histogram.get_num_headers import get_num_headers

# def print_pair_plot(values):

#     df = px.data.iris()
#     print(df)
#     fig = px.scatter_matrix(df,
#         dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
#         color="species", symbol="species",
#         title="Scatter matrix of iris data set",
#         labels={col:col.replace('_', ' ') for col in df.columns}) # remove underscore
#     fig.update_traces(diagonal_visible=False)
#     fig.show()

# import plotly.express as px

"""

"""
def print_pair_plot(values):
    print(pd.DataFrame(values))
    num_headers = get_num_headers(values)
    # fig = px.scatter_matrix(pd.DataFrame(values),
    #     dimensions=num_headers,
    #     color="species")
    # fig = ff.create_scatterplotmatrix(pd.DataFrame(values["Slytherin"]), height=2000, width=2000, color="Hogwarts House")
    # fig.show()

    fig = px.scatter_matrix(pd.DataFrame(values),
                            height=2000,
                            width=2000,
                            color="Hogwarts House",
                            title="Scatter matrix"
                            )
    fig.show()