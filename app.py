# app_instance.py
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from components.sidebar import sidebar
from components.content import content


app = Dash(
        __name__,
        suppress_callback_exceptions=True,
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])