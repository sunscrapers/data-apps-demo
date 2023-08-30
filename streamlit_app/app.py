import altair as alt
import pandas as pd
import streamlit as st

# Load data from file
df = pd.read_json("trending.json")

# Prepare chart data
trending_week_chart_data = (
    alt.Chart(
        pd.DataFrame(list(df["week"].values)),
    )
    .mark_bar()
    .encode(x=alt.X("full_name", title="Name", sort=None), y=alt.Y("stargazers_count", title="Stars count"))
    .interactive()
)
trending_month_chart_data = (
    alt.Chart(
        pd.DataFrame(list(df["month"].values)),
    )
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
