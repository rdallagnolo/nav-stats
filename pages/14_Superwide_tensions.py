import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/Superwide Tension.csv")

# Filter columns containing "TN1" in the name
columns_to_plot = [col for col in df.columns if "TN1" in col]

# Calculate the min and max of the y values
min_y = df[columns_to_plot].min().min()
max_y = df[columns_to_plot].max().max()

# Calculate the 20% higher and lower y axis max and min values
y_min = min_y * 0.80
y_max = max_y * 1.20

# Create the line plot
fig = px.line(df, x="Seq", y=columns_to_plot)

# Update layout
fig.update_layout(
    title="Superwide tension",
    xaxis_title="Sequences",
    yaxis_title="Superwide tension (tons)",
    width=1200,
    height=800,
    template='presentation',
    legend_title_text='',
    legend_traceorder='reversed',
    showlegend=True,
    legend=dict(orientation='h', y=-0.2),
    margin=dict(b=50),
    yaxis_range=[y_min, y_max]
)

# Show the plot
st.plotly_chart(fig, theme=None)