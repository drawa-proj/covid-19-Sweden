import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px



#colors
blue = px.colors.qualitative.Safe[0]
red = px.colors.qualitative.Safe[9]


df = pd.read_csv("../data/compact.csv")


swe = df[df["country"] == "Sweden"][["date", "hosp_patients", "icu_patients"]].dropna()
swe["date"] = pd.to_datetime(swe["date"])

fig = px.line(
    swe,
    x="date",
    y=["hosp_patients", "icu_patients"],
    title="Hospital & ICU Pressure",
    labels={"value": "Patients", "date": "", "variable": ""},
    color_discrete_map={
        "hosp_patients": red,
        "icu_patients": blue,
    },
    width=1200,
    height=600,
)
fig.update_xaxes(title_text="Date")

fig.write_html("../images/hospital.html")
