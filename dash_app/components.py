from typing import List
from typing import Union

import pandas as pd
import plotly.graph_objects as go
from dash import dcc

from common.constants import GithubTrendingDateRange
from common.handlers import GithubTrendingHandler
from config import cache


@cache.memoize(timeout=5 * 60)
def get_github_trending_data_frame(date_range: GithubTrendingDateRange) -> pd.DataFrame:
    return pd.DataFrame(
        GithubTrendingHandler(date_range=date_range).get_json_repos_data(),
    )


def get_github_trending_repo_row(date_range: GithubTrendingDateRange, full_name: str) -> List[Union[str, int]]:
    df_repos: pd.DataFrame = get_github_trending_data_frame(date_range=date_range)
    repo: pd.DataFrame = df_repos.loc[df_repos["full_name"] == full_name]

    if repo.empty:
        raise Exception("Repo not found")

    return list(repo.values[0])


def get_github_trending_graph(date_range: GithubTrendingDateRange) -> list:
    df_repos: pd.DataFrame = get_github_trending_data_frame(date_range=date_range)

    figure = go.Figure(
        data=[
            {
                "x": df_repos.full_name,
                "y": df_repos.trending_stars_count,
                "type": "bar",
            },
        ],
        layout={
            "xaxis": {"title": "Repository name"},
            "yaxis": {"title": "Trending stars count"},
        },
    )
    figure.update_traces(hoverinfo="none", hovertemplate=None)

    graph: dcc.Graph = dcc.Graph(
        id="trending-graph",
        style={"height": "70vh"},
        figure=figure,
        clear_on_unhover=True,
    )
    return [
        graph,
        dcc.Tooltip(id="trending-graph-tooltip"),
    ]
