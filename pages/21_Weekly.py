import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="wide", initial_sidebar_state="auto", menu_items=None)

# Load both CSV files
vessel_speed = pd.read_csv("final/Vessel Speed.csv")
weekly_speed = pd.read_csv("final/Weekly-Vessel-Speed.csv")

# Get the rows that are in 'Vessel Speed.csv' but not in 'Weekly-Vessel-Speed.csv'
missing_rows = vessel_speed[~vessel_speed['Seq'].isin(weekly_speed['Seq'])]

# Ask the user for input for 'Hdg' and 'Week' columns for missing rows
if not missing_rows.empty:
    for _, row in missing_rows.iterrows():
        seq = row['Seq']
        hdg = st.text_input(f"Enter 'Hdg' value for Seq {seq}: ")
        week = st.text_input(f"Enter 'Week' value for Seq {seq}: ")
        
        # Add the missing row to 'Weekly-Vessel-Speed.csv' with user input
        row_with_input = [row['V1 BSP m/s'], row['V1WS1 Calc'], seq, hdg, week]
        weekly_speed.loc[len(weekly_speed)] = row_with_input

    if st.button("save"):
        # Save the updated 'Weekly-Vessel-Speed.csv'
        weekly_speed["Seq"] = weekly_speed["Seq"].astype(str)
        weekly_speed["Hdg"] = weekly_speed["Hdg"].astype(str)
        weekly_speed["Week"] = weekly_speed["Week"].astype(str)

        weekly_speed.to_csv("/home/sovnav/projects/nav-stats/StreamlitApp/final/Weekly-Vessel-Speed.csv", index=False)
else:
    st.success("weekly speeds is up to date")

# Convert 'V1 BSP m/s' and 'V1WS1 Calc' from m/s to knots
weekly_speed['V1 BSP m/s'] = weekly_speed['V1 BSP m/s'] * 1.94384
weekly_speed['V1WS1 Calc'] = weekly_speed['V1WS1 Calc'] * 1.94384

# Group by 'Week' and 'Hdg' and calculate the average of 'V1 BSP m/s' and 'V1WS1 Calc'
summary_df = weekly_speed.groupby(['Week', 'Hdg']).agg({'V1 BSP m/s': 'mean', 'V1WS1 Calc': 'mean'}).reset_index()

# Rename the columns for clarity
summary_df.rename(columns={'V1 BSP m/s': 'BSP (knots)', 'V1WS1 Calc': 'WSP (knots)'}, inplace=True)

survey_average = weekly_speed.groupby('Hdg')[['V1 BSP m/s', 'V1WS1 Calc']].mean()

col1, col2 = st.columns(2, gap="small")

with col1:
    st.subheader("Weekly speed")
    st.dataframe(round(summary_df,2))

with col2:
    st.subheader("Survey speed")
    st.dataframe(round(survey_average,2))


# plotting average weekly speeds

weeks = summary_df['Week']

# Filter the dataframe to only include BSP data
bsp_df = summary_df[summary_df["BSP (knots)"].notna()]

# Filter the dataframe to only include WSP data
wsp_df = summary_df[summary_df["WSP (knots)"].notna()]

# Create the line plot
fig1 = px.line(bsp_df, x="Week", y="BSP (knots)", color="Hdg", markers=True)
# Update the layout
fig1.update_layout(
    title="Weekly average BSP",
    xaxis_title="Week",
    yaxis_title="Vessel Speed (knots)",
    width=1200,
    height=400,
    template='presentation',
    yaxis_range=[4,5],
    legend=dict(orientation='h', y=-0.2),
    margin=dict(b=50),
    xaxis=dict(
        tickvals=weeks
    )
)

# Create the line plot
fig2 = px.line(wsp_df, x="Week", y="WSP (knots)", color="Hdg", markers=True)

# Update the layout
fig2.update_layout(
    title="Weekly average BSP",
    xaxis_title="Week",
    yaxis_title="Vessel Speed (knots)",
    width=1200,
    height=400,
    template='presentation',
    yaxis_range=[4,5],
    legend=dict(orientation='h', y=-0.2),
    margin=dict(b=50),
    xaxis=dict(
        tickvals=weeks
    )
)

# Show the plot
st.plotly_chart(fig1, theme=None)

# Show the plot
st.plotly_chart(fig2, theme=None)


# Filter the dataframe to only include BSP data
line_bsp = weekly_speed[weekly_speed["V1 BSP m/s"].notna()]

# Create the line plot
fig3 = px.line(line_bsp, x="Seq", y="V1 BSP m/s", color="Hdg")
# Update the layout
fig3.update_layout(
    title="Line average BSP",
    xaxis_title="Sequence",
    yaxis_title="Vessel Speed (knots)",
    width=1200,
    height=400,
    template='presentation',
    yaxis_range=[4,5],
    legend=dict(orientation='h', y=-0.2),
    margin=dict(b=50),
    )

fig3.add_vrect(x0=1, x1=7, line_width=0, fillcolor="green", opacity=0.2)
# Add an annotation to the plot
fig3.add_annotation(x=4, y=4.8,
            text="Week 35",
            showarrow=False,
            yshift=10)

fig3.add_vrect(x0=7.1, x1=18, line_width=0, fillcolor="aqua", opacity=0.2)
fig3.add_annotation(x=12.5, y=4.8,
            text="Week 36",
            showarrow=False,
            yshift=10)

fig3.add_vrect(x0=18.1, x1=31, line_width=0, fillcolor="yellow", opacity=0.2)
fig3.add_annotation(x=25, y=4.8,
            text="Week 37",
            showarrow=False,
            yshift=10)

fig3.add_vrect(x0=31.1, x1=36, line_width=0, fillcolor="purple", opacity=0.2)
fig3.add_annotation(x=32.5, y=4.8,
            text="Week 38",
            showarrow=False,
            yshift=10)

st.plotly_chart(fig3, theme=None)

# Filter the dataframe to only include WSP data
line_wsp = weekly_speed[weekly_speed["V1WS1 Calc"].notna()]

# Create the line plot
fig4 = px.line(line_bsp, x="Seq", y="V1WS1 Calc", color="Hdg")
# Update the layout
fig4.update_layout(
    title="Line average WSP",
    xaxis_title="Sequence",
    yaxis_title="Vessel Speed (knots)",
    width=1200,
    height=400,
    template='presentation',
    yaxis_range=[4,5],
    legend=dict(orientation='h', y=-0.2),
    margin=dict(b=50),
    )

fig4.add_vrect(x0=1, x1=7, line_width=0, fillcolor="green", opacity=0.2)
# Add an annotation to the plot
fig4.add_annotation(x=4, y=4.8,
            text="Week 35",
            showarrow=False,
            yshift=10)

fig4.add_vrect(x0=7.1, x1=18, line_width=0, fillcolor="aqua", opacity=0.2)
fig4.add_annotation(x=12.5, y=4.8,
            text="Week 36",
            showarrow=False,
            yshift=10)

fig4.add_vrect(x0=18.1, x1=31, line_width=0, fillcolor="yellow", opacity=0.2)
fig4.add_annotation(x=25, y=4.8,
            text="Week 37",
            showarrow=False,
            yshift=10)

fig4.add_vrect(x0=31.1, x1=36, line_width=0, fillcolor="purple", opacity=0.2)
fig4.add_annotation(x=32.5, y=4.8,
            text="Week 38",
            showarrow=False,
            yshift=10)



st.plotly_chart(fig4, theme=None)