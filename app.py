from dash import Dash

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

if __name__ == '__main__':
    app.run(debug=True)
