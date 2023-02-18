from dash import Dash, html, ctx
import dash_mantine_components as dmc
from dash import html, Output, Input, callback
from dash.exceptions import PreventUpdate

from components.cards import create_card

app = Dash(
    __name__,
)




app.layout = dmc.MantineProvider(
	id="app-theme",
    theme={
		"colorScheme": "white",
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        dmc.Header(
            height=90,
            withBorder=True,
            style={"padding": "16px", "display": "flex", "justifyContent": "space-between"},
            children=[
                dmc.Text(
                    "Dash Application With Dark Mode",
                    style={"fontSize": 40},
                ),
                dmc.Switch(
                        id="switch-theme",
                        size="lg",
                        radius="sm",
                        label="Dark Mode",
                        checked=True
                    ),
                ],
        ),
        html.Div(
            [
                create_card(
                    image_src="https://images.unsplash.com/photo-1534972195531-d756b9bfa9f2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80",
                    title="Dash is Awesome!",
                    text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l"
                ),
                   
                create_card(
                    image_src="https://images.unsplash.com/photo-1608222351212-18fe0ec7b13b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1548&q=80",
                    title="DMC is Awesome!",
                    text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l"
                ),
                create_card(
                    image_src="https://images.unsplash.com/photo-1526379095098-d400fd0bf935?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2064&q=80",
                    title="Python as well!",
                    text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l"
                ),
                create_card(
                    image_src="https://images.unsplash.com/photo-1515871204537-49a5fe66a31f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1564&q=80",
                    title="Do not forget to follow me <3",
                    text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l"
                ),
            ],
            style={"padding": "32px", "display": "flex", "justifyContent": "space-between"}
        ),
        dmc.Divider(variant="solid"),
        html.Div(
            [
                dmc.Paper(
                    children=[
                        dmc.Text(
                            """
                            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
                            sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
                            ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore 
                            magna aliquyam erat, sed diam voluptua.
                            """
                        )
                    ],
                    p="sm",
                    radius="sm",
                    shadow="sm"
                ),
                dmc.Paper(
                    children=[
                        dmc.Text(
                            """
                            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
                            sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
                            ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore 
                            magna aliquyam erat, sed diam voluptua.
                            """
                        )
                    ],
                    p="sm",
                    radius="sm",
                    shadow="sm"
                ),
                dmc.Paper(
                    children=[
                        dmc.Text(
                            """
                            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
                            sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
                            ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore 
                            magna aliquyam erat, sed diam voluptua.
                            """
                        )
                    ],
                    p="sm",
                    radius="sm",
                    shadow="sm"
                ),
            ],
            style={"padding": "32px", "display": "flex", "justifyContent": "space-between"}
        )
    ],
)


@app.callback(
    Output('app-theme', 'theme'),
    Input('app-theme', 'theme'),
    Input("switch-theme", "checked"),
    prevent_intial_call=True)
def switch_theme(theme, checked):
    trigger = ctx.triggered[0]["prop_id"]
    if trigger == 'switch-theme.checked':
        if theme.get("colorScheme") == "white":
            theme.update({'colorScheme': 'dark'})
        else:
            theme.update({'colorScheme': 'white'})
        return theme
    raise PreventUpdate

if __name__ == "__main__":
    app.run_server(debug=True)