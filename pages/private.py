from dash import Input, Output, html, dcc, callback, register_page
import pandas as pd
import plotly.express as px

register_page(__name__, "/private")
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

layout = [
    html.H1(children='My Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')
