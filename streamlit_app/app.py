import json

import altair as alt
import pandas as pd
import streamlit as st

# Load data from file
with open("trending.json") as f:
    trending_json_data = json.load(f)

# Prepare data frames
df_week = pd.DataFrame(trending_json_data["week"])
df_month = pd.DataFrame(trending_json_data["month"])

# Prepare charts
trending_week_chart_data = (
    alt.Chart(df_week)
    .mark_bar()
    .encode(x=alt.X("full_name", title="Name", sort=None), y=alt.Y("stargazers_count", title="Stars count"))
    .interactive()
)
trending_month_chart_data = (
    alt.Chart(df_month)
    .mark_bar()
    .encode(
        x=alt.X("full_name", title="Name", sort=None),
        y=alt.Y("stargazers_count", title="Stars count"),
    )
    .interactive()
)

# Draw charts
st.title("Top Github Trending Repositories")
tab1, tab2 = st.tabs(["This week", "This month"])
with tab1:
    st.altair_chart(trending_week_chart_data, use_container_width=True)
with tab2:
    st.altair_chart(trending_month_chart_data, use_container_width=True)
