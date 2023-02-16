from dash import Dash, html, dash_table
import dash_mantine_components as dmc
from dash import html, Output, Input, callback
import pandas as pd
from time import sleep

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
        )
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

if __name__ == '__main__':
    app.run_server(debug=True)