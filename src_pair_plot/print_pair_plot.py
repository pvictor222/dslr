import plotly.express as px
import pandas as pd

"""
    Prints the features, with houses as colors
"""
def print_pair_plot(values):
    fig = px.scatter_matrix(pd.DataFrame(values),
                            height=2000,
                            width=2000,
                            color="Hogwarts House",
                            title="Scatter matrix"
                            )
    fig.show()