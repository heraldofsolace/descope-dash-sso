from dash import html, dcc, register_page

register_page(__name__, '/')

def layout():
    return [
        html.H1("Public page"),
        dcc.Link("View private page", href="/private"),
    ]
