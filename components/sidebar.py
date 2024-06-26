import dash_bootstrap_components as dbc
from dash import html
from styles.styles import SIDEBAR_STYLE


sidebar = html.Div(
    [
        html.H2("Watt/PCP", className="display-5"),
        html.Hr(),
        html.P(
            "Navegue as opções abaixo para acessar as ferramentas de PCP.", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("Ordens de Serviço", href="/os", active="exact"),
                dbc.NavLink("Requisições de Material", href="/requisicoes", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)