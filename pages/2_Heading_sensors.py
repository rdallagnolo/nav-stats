import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("../StreamlitApp/final/Gyros.csv")

# Calculate the differences between columns
df["V1GY1 - V1GY2"] = df["V1GY1 Raw °"] - df["V1GY2 Raw °"]
df["V1GY1 - V1GY3"] = df["V1GY1 Raw °"] - df["V1GY3 Raw °"]
df["V1GY2 - V1GY3"] = df["V1GY2 Raw °"] - df["V1GY3 Raw °"]

# Calculate the observed minimum and maximum values
min_y = df.iloc[:,-3:].min()
max_y = df.iloc[:,-3:].max()

# Calculate the y-axis limits (50%)
y_range = (min_y.min() * 1.5, max_y.max() * 1.5)

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
    height=600,
)

# Update the legend
fig.update_layout(
    legend_title_text='',
    legend_traceorder='reversed',
    showlegend=True,
    legend=dict(orientation='h', y=-0.2),  # Adjust the y-coordinate of the legend
    margin=dict(b=50),  # Adjust the bottom margin to make space for the legend
)

# Update the y-axis limits in the figure
fig.update_yaxes(range=y_range)

# Show the plot
st.plotly_chart(fig,theme=None)
