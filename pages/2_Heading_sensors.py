import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/Gyros.csv")

# Calculate the differences between columns
df["V1GY1 - V1GY2"] = df["V1GY1 Raw °"] - df["V1GY2 Raw °"]
df["V1GY1 - V1GY3"] = df["V1GY1 Raw °"] - df["V1GY3 Raw °"]
df["V1GY2 - V1GY3"] = df["V1GY2 Raw °"] - df["V1GY3 Raw °"]

# Calculate the min and max of the differences
min_diff = df[["V1GY1 - V1GY2", "V1GY1 - V1GY3", "V1GY2 - V1GY3"]].min().min()
max_diff = df[["V1GY1 - V1GY2", "V1GY1 - V1GY3", "V1GY2 - V1GY3"]].max().max()

# Calculate the 20% higher and lower y axis max and min values
y_min = min_diff * 1.5
y_max = max_diff * 1.5

# Create the line plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=df["Seq"], y=df["V1GY1 - V1GY2"], mode="lines", name="V1GY1 - V1GY2"))
fig.add_trace(go.Scatter(x=df["Seq"], y=df["V1GY1 - V1GY3"], mode="lines", name="V1GY1 - V1GY3"))
fig.add_trace(go.Scatter(x=df["Seq"], y=df["V1GY2 - V1GY3"], mode="lines", name="V1GY2 - V1GY3"))


# Update layout
fig.update_layout(
    title="Gyro differences",
    xaxis_title="Sequences",
    yaxis_title="Difference (°)",
    width=1200,
    height=800,
    template='presentation',
    legend_title_text='',
    legend_traceorder='reversed',
    showlegend=True,
    legend=dict(orientation='h', y=-0.2),
    margin=dict(b=50),
    yaxis_range=[y_min, y_max],
)

# Show the plot
st.plotly_chart(fig,theme=None)
