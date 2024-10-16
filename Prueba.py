import dash
from dash import dcc, html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1("Hola Dash"),
    dcc.Graph(id='example-graph')
])

# Define tus callbacks aquí, si los tienes.

if __name__ == '__main__':
    app.run_server(debug=True)
