import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/Vessel Speed.csv")

# converting to knots
df['V1 BSP m/s'] = df['V1 BSP m/s'] * 1.94384
df['V1WS1 Calc'] = df['V1WS1 Calc'] * 1.94384

columns_to_plot = df.columns[:-1]

# Calculate the min and max of the y values
min_y = df[columns_to_plot].min().min()
max_y = df[columns_to_plot].max().max()

# Calculate the 20% higher and lower y axis max and min values
y_min_20 = min_y * 0.8
y_max_20 = max_y * 1.2

# Create the line plot
fig = px.line(df, x="Seq", y=columns_to_plot)

# Update layout
fig.update_layout(
    title="Vessel speed",
    xaxis_title="Sequences",
    yaxis_title="Vessel speed (knots)",
    width=1200,
    height=800,
    template='presentation',
    legend_title_text='',
    legend_traceorder='reversed',
    showlegend=True,
    legend=dict(orientation='h', y=-0.2),
    margin=dict(b=50),
    yaxis_range=[y_min_20, y_max_20]
)

# Show the plot
st.plotly_chart(fig, theme=None)