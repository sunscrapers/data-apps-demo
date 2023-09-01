import json
from typing import Dict

import pandas as pd
from dash import Dash
from dash import Input
from dash import Output
from dash import callback
from dash import dcc
from dash import html

# Load data from file
with open("trending.json") as f:
    trending_json_data: Dict = json.load(f)

# Prepare data frames
df_week: pd.DataFrame = pd.DataFrame(trending_json_data["week"])
df_month: pd.DataFrame = pd.DataFrame(trending_json_data["month"])

# Prepare graphs
graph_week: dcc.Graph = dcc.Graph(
    figure={
        "data": [
            {
                "x": df_week.full_name,
                "y": df_week.stargazers_count,
                "type": "bar",
            },
        ],
    }
)
graph_month: dcc.Graph = dcc.Graph(
    figure={
        "data": [
            {
                "x": df_month.full_name,
                "y": df_month.stargazers_count,
                "type": "bar",
            },
        ],
    }
)

# Initialize app
app: Dash = Dash(__name__)

# Define layout of the page
app.layout = html.Div(
    [
        html.H1("Top Github Trending Repositories"),
        dcc.Tabs(
            id="tabs-example-graph",
            value="week",
            children=[
                dcc.Tab(label="This week", value="week"),
                dcc.Tab(label="This month", value="month"),
            ],
        ),
        html.Div(id="tabs-content-example-graph"),
    ]
)


# Connect tabs with graphs
@callback(
    Output("tabs-content-example-graph", "children"),
    Input("tabs-example-graph", "value"),
)
def render_content(tab):
    if tab == "week":
        return graph_week
    elif tab == "month":
        return graph_month


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
