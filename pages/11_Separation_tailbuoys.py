import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/Tailbuoy Separation .csv")

columns_to_plot = df.columns[0:-2]

# Calculate the min and max of the y values
min_y = df[columns_to_plot].min().min()
max_y = df[columns_to_plot].max().max()

# Calculate the 10% higher and lower y axis max and min values
y_min = min_y * 0.90
y_max = max_y * 1.10

fig = px.line(df, x='Seq', y=columns_to_plot)

# Update layout
fig.update_layout(
    title="Tail-buoy separation",
    xaxis_title="Sequences",
    yaxis_title="Separation (m)",
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

st.plotly_chart(fig, theme=None)