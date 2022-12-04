from dash import html, page_registry
import dash_bootstrap_components as dbc


def sidebar():
    nav_links = []
    for page in page_registry.values():
        if page["path"].startswith("/app"):
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2")
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
            print(f"added page {page['name']}")

        elif page["path"] == "/projects":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Swetrix stats", className="ms-2")
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
            print(f"added page {page['name']}")

    return dbc.Nav(children=nav_links,
                   vertical=True,
                   pills=True,
                   className="bg-dark")
