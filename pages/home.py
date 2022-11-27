import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)
layout = html.Div(
    [
        dcc.Markdown("# Oleksandr Kamenivskyy", style={"textAlign": "center"}),
        html.Hr()

    ]
)
