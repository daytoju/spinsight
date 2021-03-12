import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dbc.Row(
        dbc.Col(
            html.H1("----<===== SP Insight - JSA 2021 =====>----"),width={'size': 12, 'offset': 4}
        )
    ),

    dbc.Row(
        dbc.Col(
            html.Div("Spectrum Protect Available Datas: "),width={'size': 6, 'offset': 1}
        )
    ),
])

if __name__ == "__main__":
    app.run_server()