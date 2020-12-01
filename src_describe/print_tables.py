import plotly.graph_objects as go

"""
        GOAL: print the description tables:
        1. Numerical values
        2. Non-numerical values
"""
def print_tables(values):
    num_values = values[0]
    non_num_values = values[1]
    num_headers = values[2]
    non_num_headers = values[3]
    fig_num = go.Figure(data=[go.Table(header=dict(values=num_headers,
                                        line_color='darkslategray',
                                        fill=dict(color=['darkslategray', 'royalblue']),
                                        font=dict(color='white', size=12),
                                        align='center'),
                                cells=dict(values=num_values,
                                        line_color='darkslategray',
                                        fill=dict(color=['lightcyan', 'white']),
                                        align='center'),
                        )])
    fig_num.update_layout(
        title="Numerical values",
    )
    fig_non_num = go.Figure(data=[go.Table(header=dict(values=non_num_headers,
                                        line_color='darkslategray',
                                        fill=dict(color=['darkslategray', 'royalblue']),
                                        font=dict(color='white', size=12),
                                        align='center'),
                                cells=dict(values=non_num_values,
                                        line_color='darkslategray',
                                        fill=dict(color=['lightcyan', 'white']),
                                        align='center')
                        )])
    fig_non_num.update_layout(
        title="Non-numerical values",
    )    
    fig_num.show()
    fig_non_num.show()