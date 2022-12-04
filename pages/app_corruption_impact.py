from dash_bootstrap_components import Row, Col
from dash import dcc, html, Input, Output, callback, register_page
from assets.data_organisation import graph_1, graph_2
from pages.side_bar import sidebar

register_page(__name__, path="/app1")

layout = html.Div([
    Row(
        [
            Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2
            ),
            Col(
                [
                    dcc.Markdown("# Corruption impact on GDP per capita", style={"textAlign": "center"}, className="ml-3")
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
            )
        ]
    ),
    html.Hr(),
    dcc.Dropdown(id='year',
                 options=[{'label': '2021', 'value': '2021'}],
                 multi=False,
                 value='2021',
                 style={'width': '40%', 'color': 'black'}),
    dcc.Graph(id='graph_1'),
    dcc.Graph(id='graph_2')
])


@callback(
    Output(component_id='graph_1', component_property='figure'),
    Output(component_id='graph_2', component_property='figure'),
    Input(component_id='year', component_property='value')
)
def fill_graphs(input_value):
    # function that returns graph value depending on the input_value
    if input_value == "2021":
        return graph_1, graph_2
