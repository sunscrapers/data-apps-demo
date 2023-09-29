from dash import dcc
from dash import html

from callbacks import *  # noqa
from common.constants import GithubTrendingDateRange
from components import get_github_trending_graph
from config import app

# Define layout of the page
app.layout = html.Div(
    [
        html.H1("Github Trending Python Repositories"),
        dcc.Tabs(
            id="tabs-trending-graph",
            value=GithubTrendingDateRange.daily.value,
            children=[
                dcc.Tab(label="Today", value=GithubTrendingDateRange.daily.value),
                dcc.Tab(label="This week", value=GithubTrendingDateRange.weekly.value),
                dcc.Tab(label="This month", value=GithubTrendingDateRange.monthly.value),
            ],
        ),
        html.Div(
            get_github_trending_graph(date_range=GithubTrendingDateRange.daily),
            id="tabs-content-trending-graph",
        ),
    ]
)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # nosec
