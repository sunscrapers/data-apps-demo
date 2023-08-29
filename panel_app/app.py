import hvplot.pandas  # noqa
import pandas as pd
import panel as pn

pn.extension("tabulator", sizing_mode="stretch_width")

PALETTE = [
    "#ff6f69",
    "#ffcc5c",
    "#88d8b0",
]
ACCENT_BASE_COLOR = PALETTE[0]
URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
LOCAL_FILE = "rows.csv"

INFO = f"""\
## Widgets as arguments in your Pandas pipeline!
"""
SOURCE_INFO = f"""\
## Data
Bicycle counts on Seattle's Fremont Bridge
"""
# Data
try:
    seattle_bikes = pd.read_csv(LOCAL_FILE, parse_dates=["Date"]).set_index("Date")
except Exception:
    seattle_bikes = pd.read_csv(URL, parse_dates=["Date"]).set_index("Date")
    seattle_bikes.to_csv(LOCAL_FILE)

# Widgets
resample = pn.widgets.Select(value="D", options=["D", "W", "M"], name="Sampling Frequency")
window = pn.widgets.IntSlider(value=50, start=10, end=100, name="Rolling Window Length")
center = pn.widgets.Checkbox(value=True, name="Center")
win_type = pn.widgets.Select(value="gaussian", options=[None, "gaussian"], name="Window Type")
std = pn.widgets.IntSlider(value=10, start=5, end=20, name="std")
line_width = pn.widgets.IntSlider(value=6, start=1, end=20, name="Line Width")

# A Pandas Dataframe made .interactive with hvPlot
pipeline = (
    seattle_bikes.interactive()
    .resample(resample)
    .sum()
    .rolling(window, center=center, win_type=win_type)
    .sum(std=std)
    .dropna()
)

# Interactive Plot
plot = pn.panel(
    pipeline.hvplot(
        responsive=True,
        color=PALETTE,
        line_width=line_width,
        yformatter="%.0f",
    )
    .holoviews()
    .opts(legend_position="top_left"),
    sizing_mode="stretch_both",
    name="Plot",
)

# Interactive Table
table = pipeline.pipe(
    pn.widgets.Tabulator,
    pagination="remote",
    page_size=20,
    theme="fast",
    sizing_mode="stretch_both",
).panel(name="Table")

# Layout
tabs = pn.layout.Tabs(plot, table, margin=(10, 25), sizing_mode="stretch_both")
panel_logo = pn.pane.PNG(
    "https://panel.holoviz.org/_static/logo_stacked.png",
    link_url="https://panel.holoviz.org",
    embed=False,
    sizing_mode="fixed",
    height=100,
    margin=(10, 10),
    align="start",
)
hvplot_logo = pn.pane.PNG(
    "https://hvplot.holoviz.org/assets/hvplot-wm.png",
    link_url="https://hvplot.holoviz.org/",
    embed=False,
    sizing_mode="fixed",
    height=100,
    margin=(10, 10),
    align="center",
)
pandas = pn.pane.HTML("<div style='font-size: 100px;text-align: center'>🐼</div>", height=100, margin=(10, 5, 10, 5))
pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Hvplot makes your Pandas pipeline .interactive",
    sidebar=[
        SOURCE_INFO,
        "## Pandas Pipeline",
        resample,
        window,
        center,
        win_type,
        std,
        "## Plot",
        line_width,
        pn.Spacer(height=150),
        pn.Row(panel_logo, hvplot_logo),
        pandas,
    ],
    main=[INFO, tabs],
    accent_base_color=ACCENT_BASE_COLOR,
    header_background=ACCENT_BASE_COLOR,
).servable()
