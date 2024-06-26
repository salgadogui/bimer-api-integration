from dash import html, dcc, callback, Output, Input
from app import app
from views.dashboard_view import dashboard_view
from views.production_orders_view import production_orders_view
from views.material_requisitions_view import material_requisitions_view

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dashboard_view()
    elif pathname == "/os":
        return production_orders_view()
    elif pathname == "/requisicoes":
        return material_requisitions_view()
    
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )
