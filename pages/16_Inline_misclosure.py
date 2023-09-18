import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/Streamer Inline Misclosure.csv")

# Assuming df is your DataFrame
columns_to_plot = df.columns[:]

fig = px.line(df, x='Seq', y=columns_to_plot,
              labels={'Seq': 'Sequence'},
              )
fig.update_traces(line=dict(width=2))  # Adjust line width if needed

# Update layout
fig.update_layout(
    title="Inline Misclosure",
    xaxis_title="Sequences",
    yaxis_title="Misclosure (m)",
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


st.plotly_chart(fig, theme=None)