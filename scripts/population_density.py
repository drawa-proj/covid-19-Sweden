#population density ppl/km^2

import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "Country": ["Sweden", "Finland", "Norway", "Denmark", "New Zealand"],
    "Population_Density": [23, 16, 14, 135, 19.9]
})


#colors
blue = px.colors.qualitative.Safe[0]
red = px.colors.qualitative.Safe[9]
cyan = px.colors.qualitative.D3[4]
green = px.colors.qualitative.Bold[5]
darkblue = px.colors.qualitative.G10[9]


df = df.sort_values("Population_Density")

fig = px.bar(
    df,
    x="Population_Density",
    y="Country",
    orientation="h",
    text="Population_Density",
    title="Population density in selected countries",
    labels={
        "Population_Density": "People per km²",
        "Country": ""
    },
    color = "Country",
    color_discrete_sequence=[blue,darkblue,red,cyan,green],

)

fig.update_traces(
    textposition="outside"
)


fig.update_layout(
    width=1000,
    height=500,
    showlegend=False,
)
fig.write_html("../images/population_density.html")