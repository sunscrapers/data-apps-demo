import json
from typing import Dict

import hvplot.pandas  # noqa
import pandas as pd
import panel as pn
from holoviews.element import chart

# Load data from file
with open("trending.json") as f:
    trending_json_data: Dict = json.load(f)

# Prepare data frames
df_week: pd.DataFrame = pd.DataFrame(trending_json_data["week"])
df_month: pd.DataFrame = pd.DataFrame(trending_json_data["month"])

# Prepare charts
chart_week: chart.Bars = df_week.hvplot.bar(
    x="full_name",
    y="stargazers_count",
    xlabel="Full repository name",
    ylabel="Stars count",
    responsive=True,
).opts(xrotation=90)

chart_month: chart.Bars = df_month.hvplot.bar(
    x="full_name",
    y="stargazers_count",
    xlabel="Full repository name",
    ylabel="Stars count",
    responsive=True,
).opts(xrotation=90)


# Prepare tabs to allow switching between charts
tabs: pn.Tabs = pn.Tabs(
    ("This week", pn.pane.HoloViews(chart_week, linked_axes=False)),
    ("This month", chart_month),
)

# Render charts
pn.template.FastListTemplate(
    title="Top Github Trending Repositories",
    main=[tabs],
).servable()
