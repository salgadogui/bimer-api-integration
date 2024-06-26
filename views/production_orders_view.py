from dash import html, dcc, Output, Input
import plotly.express as px
import modules.production as production
from app import app
import dash_ag_grid as dag
from components import dropdown


def production_orders_view():
    df = production.getProductionOrders()

    return html.P("This is the content of page 1. Yay!")