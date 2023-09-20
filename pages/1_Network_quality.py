import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/NQ Main.csv")

# Calculate the 20% higher and lower y axis max and min values
y_min = df["main Quality"].min()
y_max = df["main Quality"].max()
y_min = y_min * 0.5
y_max = y_max * 1.5

# Create the line plot using Plotly Express
fig = px.line(df, x="Seq", y="main Quality")

# Update layout
fig.update_layout(
    title="Network Quality (Main)",
    xaxis_title="Sequences",
    yaxis_title="Quality",
    width=1200,
    height=800,
    template='presentation',
    legend_title_text='',
    legend_traceorder='reversed',
    showlegend=True,
    legend=dict(orientation='h', y=-0.2),  # Adjust the y-coordinate of the legend
    margin=dict(b=50),  # Adjust the bottom margin to make space for the legend
    yaxis_range=[y_min, y_max]
)

# Show the plot
st.plotly_chart(fig, theme=None)
st.write(df)
