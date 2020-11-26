import plotly.graph_objects as go

def print_tables(values):
    num_values = values[0]
    non_num_values = values[1]
    num_headers = values[2]
    non_num_headers = values[3]
    print(num_headers)
    print(num_values)
    print(non_num_headers)
    print(non_num_values)
    fig_num = go.Figure(data=[go.Table(header=dict(values=num_headers,
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                        cells=dict(values=num_values,
                                line_color='darkslategray',
                                fill_color='lightcyan',
                                align='left'),
                        )])
    fig_non_num = go.Figure(data=[go.Table(header=dict(values=non_num_headers,
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                        cells=dict(values=non_num_values,
                                line_color='darkslategray',
                                fill_color='lightcyan',
                                align='left')
                        )])
    fig_num.show()
    fig_non_num.show()