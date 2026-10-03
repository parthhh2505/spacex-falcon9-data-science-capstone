import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

DATA_URL = "https://raw.githubusercontent.com/adgsenpai/IBM-DataScience-SpaceX-Capstone/main/dataset_part_2.csv"

def load_data():
    local = os.path.join(os.path.dirname(__file__), "..", "data", "spacex_cleaned.csv")
    df = pd.read_csv(local) if os.path.exists(local) else pd.read_csv(DATA_URL)
    df["PayloadMass"] = df["PayloadMass"].fillna(df["PayloadMass"].mean())
    return df

df = load_data()
app = Dash(__name__)
app.title = "SpaceX Falcon 9 Landing Dashboard"

app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Launch & Landing Dashboard"),
    html.P("Interactive analysis of launch sites, payloads and first-stage landing outcomes."),
    html.Label("Launch Site"),
    dcc.Dropdown(
        id="site",
        options=[{"label":"All Sites","value":"ALL"}] +
                [{"label":x,"value":x} for x in sorted(df["LaunchSite"].unique())],
        value="ALL", clearable=False
    ),
    html.Br(),
    html.Label("Payload Range (kg)"),
    dcc.RangeSlider(
        id="payload",
        min=float(df["PayloadMass"].min()),
        max=float(df["PayloadMass"].max()),
        value=[float(df["PayloadMass"].min()), float(df["PayloadMass"].max())]
    ),
    dcc.Graph(id="success-pie"),
    dcc.Graph(id="payload-scatter")
])

@app.callback(
    Output("success-pie","figure"),
    Output("payload-scatter","figure"),
    Input("site","value"),
    Input("payload","value")
)
def update(site, payload):
    filtered = df[(df["PayloadMass"] >= payload[0]) & (df["PayloadMass"] <= payload[1])].copy()
    if site != "ALL":
        filtered = filtered[filtered["LaunchSite"] == site]

    counts = filtered["Class"].value_counts().rename(index={0:"Unsuccessful",1:"Successful"})
    pie = px.pie(values=counts.values, names=counts.index, title="Landing Outcome")

    scatter = px.scatter(
        filtered, x="PayloadMass", y="Class", color="Orbit",
        hover_data=["FlightNumber","LaunchSite"],
        title="Payload Mass vs Landing Outcome"
    )
    return pie, scatter

if __name__ == "__main__":
    app.run(debug=True)
