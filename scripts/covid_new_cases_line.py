#2nd plot, intearctive line plot, new cases

import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/compact.csv")
countries = ["Norway", "Finland", "Sweden", "Denmark", "New Zealand"]

#colors
blue = px.colors.qualitative.Safe[0]
red = px.colors.qualitative.Safe[9]
cyan = px.colors.qualitative.D3[4]
green = px.colors.qualitative.Bold[5]
darkblue = px.colors.qualitative.G10[9]


cdf = df[df["country"].isin(countries)].copy()
cdf = cdf[["country", "date", "new_cases_per_million"]].dropna()
cdf["date"] = pd.to_datetime(cdf["date"])

cdf["month"] = cdf["date"].dt.to_period("M").dt.to_timestamp()
cdf = cdf.groupby(["country", "month"])["new_cases_per_million"].max().reset_index()
cdf["month_str"] = cdf["month"].dt.strftime("%b %Y")

fig = px.line(
    cdf,
    x="month",
    y="new_cases_per_million",
    color="country",
    title="COVID-19 new cases",
    labels={"new_cases_per_million": "new cases per million", "month": "year"},
    color_discrete_sequence=[cyan,darkblue,green,blue,red],
    width=1200,
    height=600,
    
)
fig.write_html("../images/covid_new_cases_line.html")

