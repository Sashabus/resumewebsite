from dash import Dash, page_registry, page_container
from dash_bootstrap_components import themes, Navbar, Container, Row, Nav, NavLink

app = Dash(__name__, use_pages=True, external_stylesheets=[themes.SUPERHERO])
server = app.server

header = Navbar(
    Container(
        [
            Row(
                [
                    Nav(
                        [

                            NavLink(page["name"], href=page["path"])
                            for page in page_registry.values()
                            if not page["path"].startswith("/app")
                            # for every page in page registry, if its name doesn't start with /app create link in the
                            # header of the app in the row
                        ]
                    ),
                ]
            )
        ],
        fluid=True,
    ),
    dark=True,
    color="dark",
)

app.layout = Container([header, page_container], fluid=False)

if __name__ == "__main__":
    app.run_server()
