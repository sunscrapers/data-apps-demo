from typing import Any
from typing import Dict
from typing import List

from dash import Input
from dash import Output
from dash import State
from dash import callback
from dash import html
from dash import no_update

from common.constants import GithubTrendingDateRange
from components import get_github_trending_graph
from components import get_github_trending_repo_row


# Return proper graph (children) for chosen tab
@callback(
    Output("tabs-content-trending-graph", "children"),
    Input("tabs-trending-graph", "value"),
)
def github_repos_render_graph(tab) -> list:
    date_range: GithubTrendingDateRange = GithubTrendingDateRange.daily
    if tab == GithubTrendingDateRange.weekly.value:
        date_range = GithubTrendingDateRange.weekly
    if tab == GithubTrendingDateRange.monthly.value:
        date_range = GithubTrendingDateRange.monthly

    return get_github_trending_graph(date_range=date_range)


@callback(
    Output("trending-graph-tooltip", "show"),
    Output("trending-graph-tooltip", "bbox"),
    Output("trending-graph-tooltip", "children"),
    Input("trending-graph", "hoverData"),
    State("tabs-trending-graph", "value"),
)
def github_repos_graph_display_hover(hover_data: Dict[str, Any], trending_graph_tab: str) -> tuple:
    if hover_data is None:
        return False, no_update, no_update

    pt: Dict[str, Any] = hover_data["points"][0]
    date_range: GithubTrendingDateRange = GithubTrendingDateRange(trending_graph_tab)
    full_name, stars_count, trending_stars_count = get_github_trending_repo_row(
        date_range=date_range, full_name=pt["label"]
    )

    children: List[html.Div] = [
        html.Div(
            [
                html.P(f"Repository name: {full_name}"),
                html.P(f"Stars count: {stars_count}"),
                html.P(f"Trending stars count: {trending_stars_count}"),
            ],
        )
    ]

    return True, pt["bbox"], children
