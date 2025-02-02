from dash import Input, Output, html, dcc, callback, register_page
from dash_auth import public_callback
import pandas as pd
import plotly.express as px
from flask import session

register_page(__name__, "/private")
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

def layout():
    user = session["user"]
    return [
        html.H1(children=f'Welcome {user["email"]}', style={'textAlign':'center'}),
        dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
        dcc.Graph(id='graph-content'),
        dcc.Link("Log out", href="/oidc/logout", refresh=True)
    ]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')
