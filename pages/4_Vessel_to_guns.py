import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/Vessel to Gun and Streamer.csv")

# Assuming df is your DataFrame
columns_to_plot = df.columns[:-1][:3]  # Select the first 3 columns

# Calculate the min and max of the y values
min_y = df[columns_to_plot].min().min()
max_y = df[columns_to_plot].max().max()

# Calculate the 5% higher and lower y axis max and min values
y_min = min_y * 0.95
y_max = max_y * 1.05

fig = px.line(df, x='Seq', y=columns_to_plot, title='Line Plot of Selected Columns',
              labels={'Seq': 'Sequence'},
              )
fig.update_traces(line=dict(width=2))  # Adjust line width if needed

# Update layout
fig.update_layout(
    title="Distance vessel to guns",
    xaxis_title="Sequences",
    yaxis_title="Distance(m)",
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

st.plotly_chart(fig, theme = None)
#st.write(max_y)
