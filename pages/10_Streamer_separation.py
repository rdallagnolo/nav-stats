import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)


df = pd.read_csv("../StreamlitApp/final/Streamer Separation.csv")

fig = px.line(df, x='Seq', y=df.columns[0:-2], title='Streamer head separation', width=1200, height=600)
fig.update_xaxes(title_text='Sequence')
fig.update_yaxes(title_text='Separation (m)')

# Update the legend
fig.update_layout(
    legend_title_text='',
    legend_traceorder='reversed',
    showlegend=True,
    legend=dict(orientation='h', y=-0.2),  # Adjust the y-coordinate of the legend
    margin=dict(b=50),  # Adjust the bottom margin to make space for the legend
)

st.plotly_chart(fig,theme=None)
