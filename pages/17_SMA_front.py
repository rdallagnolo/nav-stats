import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("../StreamlitApp/final/SMAs.csv")

# Select the first 18 columns for the plot
columns_to_plot = df.columns[0:18]  # Assuming the first column is "Seq"

# Create the line plot
fig = px.line(df, x="Seq", y=columns_to_plot)

# Update layout
fig.update_layout(
    title="SMA front nodes",
    xaxis_title="Sequences",
    yaxis_title="SMA (m)",
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


# Show the plot
st.plotly_chart(fig, theme=None)