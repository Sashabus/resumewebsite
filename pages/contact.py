import dash
from dash import dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2)

green_rext = {"color": "green"}


def layout():
    return dbc.Row(
        [
            dbc.Col(
                [
                    dcc.Markdown("# Oleksandr Kamenivskyy", className="mt-3"),
                    dcc.Markdown("### Student", className="mb-5"),
                    dcc.Markdown("### Personal info", style={"color": "gray"}),
                    dcc.Markdown("Address", style=green_rext),
                    dcc.Markdown("Miskolc, Hungary 70565"),
                    dcc.Markdown("Phone nuber", style=green_rext),
                    dcc.Markdown("+380989655648"),
                    dcc.Markdown("Email", style=green_rext),
                    dcc.Markdown("vsashabus4321@gmail.com")

                ],
                width={"size": 6, "offset": 2},
            )
        ],
        justify="center",
    )
