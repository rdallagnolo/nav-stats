import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/Vessel to Gun and Streamer.csv")

# Assuming df is your DataFrame
columns_to_plot = df.columns[:-1][:3]  # Select the first 3 columns

# Calculate the observed minimum and maximum values
min_y = df.iloc[:,:3].min()
max_y = df.iloc[:,:3].max()

# Calculate the y-axis limits (3%)
y_range = (min_y.min() * 0.97, max_y.max() * 1.03)


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

# Update the y-axis limits in the figure
fig.update_yaxes(range=y_range)

st.plotly_chart(fig, theme = None)
