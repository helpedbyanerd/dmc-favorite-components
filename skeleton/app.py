from dash import Dash, html, dash_table
import dash_mantine_components as dmc
from dash import html, Output, Input, callback
import pandas as pd
from time import sleep

from components.cards import create_card

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
)


app.layout = html.Div(children=[
        html.Div(
            [
                dmc.Skeleton(
                    visible=False,
                    children=html.Div(id="skeleton-datatable-container"),
                    mb=10,
                ),
                dmc.Button("Click Me!", id="datatable-skeleton-button"),
            ],
            style={"padding": "32px"}
        ),
        html.Div(
            [
                dmc.Skeleton(
                    visible=False,
                    height=500,
                    width=475,
                    children=html.Div(id="skeleton-card-1-container"),
                ),
                dmc.Skeleton(
                    visible=False,  
                    height=500,
                    width=475,
                    children=html.Div(id="skeleton-card-2-container"),
                ),
                dmc.Skeleton(
                    visible=False,
                    height=500,
                    width=475,
                    children=html.Div(id="skeleton-card-3-container"),
                ),
                dmc.Skeleton(
                    visible=False,
                    height=500,
                    width=475,
                    children=html.Div(id="skeleton-card-4-container"),
                ),
            ],
            style={"padding": "32px", "display": "flex", "justifyContent": "space-between"}
        ),
        dmc.Button("Click Me!", id="card-skeleton-button"),
    ]
)





@callback(
    Output("skeleton-datatable-container", "children"),
    Input("datatable-skeleton-button", "n_clicks")
)
def create_table(n_clicks):
    url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
    df = pd.read_csv(url)
    table = dash_table.DataTable(
        id="table",
        data=df.to_dict('records'),
        columns=[{"name": col, "id": col} for col in df.columns],
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={
            'minWidth': '60px', 'width': '60px', 'maxWidth': '60px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        }
    )
    sleep(3)
    return table


@callback(
    Output("skeleton-card-1-container", "children"),
    Output("skeleton-card-2-container", "children"),
    Output("skeleton-card-3-container", "children"),
    Output("skeleton-card-4-container", "children"),
    Input("card-skeleton-button", "n_clicks")
)
def create_table(n_clicks):
    card_1 = create_card(
        image_src="https://images.unsplash.com/photo-1534972195531-d756b9bfa9f2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80",
        title="Dash is Awesome!",
        text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l"
    )
        
    card_2 = create_card(
        image_src="https://images.unsplash.com/photo-1608222351212-18fe0ec7b13b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1548&q=80",
        title="DMC is Awesome!",
        text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l"
    )

    card_3 = create_card(
        image_src="https://images.unsplash.com/photo-1526379095098-d400fd0bf935?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2064&q=80",
        title="Python as well!",
        text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l"
    )

    card_4 = create_card(
        image_src="https://images.unsplash.com/photo-1515871204537-49a5fe66a31f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1564&q=80",
        title="Do not forget to follow me <3",
        text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l"
    )
    sleep(3)

    return card_1, card_2, card_3, card_4

if __name__ == '__main__':
    app.run_server(debug=True)