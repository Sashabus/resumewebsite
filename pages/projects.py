import dash
from dash import html, dcc, Output, Input, callback
from assets.Stats import *
from pages.side_bar import sidebar
import json
import pandas as pd
import dash_bootstrap_components as dbc

with open('assets/data.json') as json_data:
    data = json.load(json_data)

main_data = pd.DataFrame(data['data'])

dash.register_page(__name__, order=1, path="/projects")

layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2
            ),
            dbc.Col(
                [
                    dcc.Markdown("# Swetrix statistics", style={"textAlign": "center"},
                                 className="ml-3")
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
            )
        ]
    ),
    html.Hr(),
    dcc.Dropdown(id='select_graph',
                 options=[{"label": "Time", "value": "time"},
                          {"label": "Advertisement", "value": "advertisement"},
                          {"label": "Country", "value": "country"}],
                 multi=False,
                 value="time",
                 style={"width": "40%", "color": "black"}),
    dcc.Graph(id='graph'),
])

aver_time_graph = Time.get_aver_graph(main_data)
advertisement_graph = get_advertisement_graph(main_data)
country_graph = Country.get_country_graph(main_data)


@callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='select_graph', component_property='value')
)
def update_graph(input_value):
    if input_value == "time":
        return aver_time_graph
    elif input_value == "advertisement":
        return advertisement_graph
    elif input_value == "country":
        return country_graph
