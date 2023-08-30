import pandas as pd
from dash import Dash
from dash import Input
from dash import Output
from dash import callback
from dash import dcc
from dash import html

# Load data from file
df = pd.read_json("trending.json")

# Initialize app
app = Dash(__name__)

# Define layout
app.layout = html.Div(
    [
        dcc.Graph(id="graph-content", config={}, style={"margin-bottom": "15px"}),
        dcc.Dropdown(df.keys(), "month", id="dropdown-selection"),
    ]
)

# Connect dropdown with graph and fill graph with data
@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    dff = df[value]

    return {
        "data": [
            {
                "x": [row["full_name"] for row in dff],
                "y": [row["stargazers_count"] for row in dff],
                "type": "bar",
            },
        ],
        "layout": {"title": "Top Github Trending Repositories"},
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
