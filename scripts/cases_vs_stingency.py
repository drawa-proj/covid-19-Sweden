import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px



#colors
blue = px.colors.qualitative.Safe[0]
red = px.colors.qualitative.Safe[9]


df = pd.read_csv("../data/compact.csv")

swe = df[df["country"] == "Sweden"][["date", "new_cases_smoothed", "stringency_index"]].dropna()
swe["date"] = pd.to_datetime(swe["date"])

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(x=swe["date"], y=swe["new_cases_smoothed"],
    name="New Cases (smoothed)", line=dict(color=red)), secondary_y=False)

fig.add_trace(go.Scatter(x=swe["date"], y=swe["stringency_index"],
    name="Stringency Index", line=dict(color=blue)), secondary_y=True)
fig.update_xaxes(title_text="Date")
fig.update_layout(title="Cases vs Government Stringency", width=1200, height=600)
fig.update_yaxes(title_text="New Cases (smoothed)", secondary_y=False) 
fig.update_yaxes(title_text="Stringency Index)", secondary_y=True)
fig.write_html("../images/cases_vs_strinency.html")
