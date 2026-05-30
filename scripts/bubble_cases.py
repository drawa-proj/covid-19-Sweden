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


df_density = pd.DataFrame({
    "country": ["Sweden", "Finland", "Norway", "Denmark", "New Zealand"],
    "population_density": [23, 16, 14, 135, 19.9]
})


df2 = df[df["country"].isin(countries)].copy()


df2 = df2[
    (pd.to_datetime(df2["date"]) >= "2020-05-01") &
    (pd.to_datetime(df2["date"]) <= "2024-08-30")
]


df2["month"] = pd.to_datetime(df2["date"]).dt.to_period("M").dt.to_timestamp()

#aggregatig to avoid traces (daily data but monthly animation) 
#getting maximum monthly values
df2 = (
    df2.groupby(["country", "month"])
       .agg(
           total_cases_per_million=("total_cases_per_million", "max")
       )
       .reset_index()
)

#adding density
df2 = df2.merge(df_density, on="country", how="left")

df2["month_str"] = df2["month"].dt.strftime("%b %Y")


fig = px.scatter(
    df2,
    x="total_cases_per_million",
    y="country",
    size="population_density",
    color="country",
    color_discrete_sequence=[blue,darkblue,red,cyan,green],
    animation_frame="month_str",
    title="COVID-19 cases vs population density",
    size_max=80,
    #not alphabetically
    category_orders={
        "country": [
            "Norway",
            "Finland",
            "Sweden",
            "Denmark",
            "New Zealand"
        ]},
        labels={
        "total_cases_per_million": "total COVID-19 cases per million",
        "country": ""
    }
)

fig.update_xaxes(
    range=[0, df2["total_cases_per_million"].max() * 1.1]
)

fig.write_html(
    "../images/density_vs_cases_bubble.html",
    auto_play=False
)