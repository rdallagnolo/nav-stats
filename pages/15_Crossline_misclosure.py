import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/Streamer Crossline Misclosure.csv")

columns_to_plot = df.columns[:-1]

# Calculate the min and max of the y values
min_y = df[columns_to_plot].min().min()
max_y = df[columns_to_plot].max().max()

# Calculate the 30% higher and lower y axis max and min values
y_min = min_y * 1.30
y_max = max_y * 1.30

fig = px.line(df, x='Seq', y=columns_to_plot,
              labels={'Seq': 'Sequence'},
              )
fig.update_traces(line=dict(width=2))  # Adjust line width if needed

# Update layout
fig.update_layout(
    title="Crossline Misclosure",
    xaxis_title="Sequences",
    yaxis_title="Misclosure (m)",
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