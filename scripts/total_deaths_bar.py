#1st plot, deaths per milion

import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/compact.csv")
countries = ["Norway", "Sweden", "Finland", "Denmark", "New Zealand"]

#colors
blue = px.colors.qualitative.Safe[0]
red = px.colors.qualitative.Safe[9]
cyan = px.colors.qualitative.D3[4]
green = px.colors.qualitative.Bold[5]
darkblue = px.colors.qualitative.G10[9]

df_deaths = df[df["country"].isin(countries)].copy()
df_deaths = df_deaths[["country", "date", "total_deaths_per_million"]].dropna()
df_deaths["date"] = pd.to_datetime(df_deaths["date"])



df_deaths["month"] = df_deaths["date"].dt.to_period("M").dt.to_timestamp()
df_deaths = df_deaths.groupby(["country", "month"])["total_deaths_per_million"].max().reset_index()
df_deaths["month_str"] = df_deaths["month"].dt.strftime("%b %Y")

fig = px.bar(
    df_deaths,
    x="country",
    y="total_deaths_per_million",
    color="country",
    animation_frame="month_str",
    range_y=[0, df_deaths["total_deaths_per_million"].max() * 1.1],
    title="COVID-19 Total Deaths",
    labels={"total_deaths_per_million": "Total deaths per milion", "country": ""},
    color_discrete_sequence=[cyan,darkblue,green,blue,red])


fig.update_xaxes(categoryorder="array", categoryarray=["Norway", "Finland", "Sweden", "Denmark", "New Zealand"])

fig.update_layout(
    showlegend=False,
    sliders=[{
        "currentvalue": {
            "prefix": "",
            "visible": True,
            "xanchor": "left",
            "font": {"size": 32, "color": "gray"},
        },
        "font": {"size": 14},
    }],
    width=1200,
    height=600,
    )
fig.write_html("../images/covid_deaths_bar.html", auto_play=False)
