import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df1 = pd.read_csv("final/Tailbuoy Separation .csv")
df2 = pd.read_csv("final/Streamer Separation.csv")

# Calculate the min and max of the y values
min_y = df2.iloc[:, -2].min()
max_y = df1.iloc[:, -2].max()

# Calculate the 5% higher and lower y axis max and min values
y_min = min_y * 0.95
y_max = max_y * 1.05

# Create a figure
fig = go.Figure()

# Add traces for the penultimate columns of the first dataframe
fig.add_trace(go.Scatter(x=df1['Seq'], y=df1.iloc[:, -2], mode='lines', name='TB01-TB12'))

# Add traces for the penultimate columns of the second dataframe
fig.add_trace(go.Scatter(x=df2['Seq'], y=df2.iloc[:, -2], mode='lines', name='S01-S12'))

# Customize the layout
fig.update_layout(
    title='Total separation Head and Tail',
    xaxis_title='Sequence',
    yaxis_title='Separation (m)',
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
st.plotly_chart(fig,theme=None)
