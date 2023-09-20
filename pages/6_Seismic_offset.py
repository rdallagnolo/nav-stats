import plotly.express as px
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("final/Vessel to Gun and Streamer.csv")
df2 = pd.read_csv("final/Inline Offsets.csv")

# Calculate the difference between the specified columns
df['Difference'] = ((df["V1 - S06 CNG DA m"] + df["V1 - S07 CNG DA m"])/2) - ((df["V1 - G1 DA m"] + df["V1 - G2 DA m"] + df["V1 - G3 DA m"])/3)
df2['Difference 2'] = (df2["(V1 DA) - (S06 DA) m"] - df2["(V1 DA) - (G2 DA) m"])

# Calculate the min and max of the y values
min_y = df['Difference'].min()
max_y = df['Difference'].max()

# Calculate the 20% higher and lower y axis max and min values
y_min = min_y * 0.80
y_max = max_y * 1.20

# Create a figure
fig = go.Figure()

# Add traces for the penultimate columns of the first dataframe
fig.add_trace(go.Scatter(x=df['Seq'], y=df['Difference'], mode='lines', name='Average seismic offset from D-along'))

# Add traces for the penultimate columns of the second dataframe
fig.add_trace(go.Scatter(x=df2['Seq'], y=df2['Difference 2'], mode='lines', name='Average seismic offset from positions'))

# Customize the layout
fig.update_layout(
    title='Seismic offset',
    xaxis_title='Sequence',
    yaxis_title='Seismic offset (m)',
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