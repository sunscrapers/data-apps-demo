import hvplot.pandas  # noqa
import pandas as pd
import panel as pn
from holoviews.element import chart

from common.constants import GithubTrendingDateRange
from common.handlers import GithubTrendingHandler


@pn.cache(ttl=5 * 60)
def get_github_trending_chart(date_range: str) -> chart.Bars:
    df_repos: pd.DataFrame = pd.DataFrame(
        GithubTrendingHandler(date_range=GithubTrendingDateRange(date_range)).get_json_repos_data(),
    )
    df_repos = df_repos.rename(
        columns={
            "full_name": "Repository name",
            "stars_count": "Stars count",
            "trending_stars_count": "Trending stars count",
        }
    )

    chart_repos: chart.Bars = df_repos.hvplot.bar(
        x="Repository name",
        y="Trending stars count",
        xlabel="Full repository name",
        hover_cols=["Repository name", "Stars count", "Trending stars count"],
        responsive=True,
    ).opts(xrotation=90)
    return chart_repos


# Prepare charts
chart_repos_daily: chart.Bars = get_github_trending_chart(date_range=GithubTrendingDateRange.daily.value)
chart_repos_weekly: chart.Bars = get_github_trending_chart(date_range=GithubTrendingDateRange.weekly.value)
chart_repos_monthly: chart.Bars = get_github_trending_chart(date_range=GithubTrendingDateRange.monthly.value)

# Prepare tabs to allow switching between charts
tabs: pn.Tabs = pn.Tabs(
    ("Today", pn.pane.HoloViews(chart_repos_daily, linked_axes=False)),
    ("This week", pn.pane.HoloViews(chart_repos_weekly, linked_axes=False)),
    ("This month", chart_repos_monthly),
)

# Render charts
pn.template.FastListTemplate(
    title="Top Github Trending Repositories",
    main=[tabs],
).servable()
