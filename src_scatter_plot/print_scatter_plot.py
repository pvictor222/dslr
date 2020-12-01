import plotly.graph_objects as go
"""
    Print the scatter plot with one trace per house
"""
def print_scatter_plot(values, max_cor):
    fig = go.Figure()
    for house in values:
        fig.add_trace(go.Scatter(x=values[house][max_cor[1]],
                                y=values[house][max_cor[2]],
                                mode='markers',
                                name=house)
                )
    fig.update_layout(
        xaxis_title=max_cor[1],
        yaxis_title=max_cor[2],
        legend_title="Hogwarts Houses",
        title="Scatter plot"
    )
    fig.show()