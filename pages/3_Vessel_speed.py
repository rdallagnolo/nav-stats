import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)


df = pd.read_csv("final/Vessel Speed.csv")
columns_to_plot = df.columns[:]


# Calculate the observed minimum and maximum values
min_y = df.iloc[:,:-1].min()
max_y = df.iloc[:,:-1].max()

# Calculate the y-axis limits (50%)
y_range = (min_y.min() * 0.5, max_y.max() * 1.5)


# Create the line plot
fig = px.line(df, x="Seq", y=columns_to_plot)

# Update layout
fig.update_layout(
    title="Vessel speed",
    xaxis_title="Sequences",
    yaxis_title="Vessel speed (knots)",
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

# Show the plot
st.plotly_chart(fig, theme=None)
st.write(df)