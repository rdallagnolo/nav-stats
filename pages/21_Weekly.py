import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="centered", initial_sidebar_state="auto", menu_items=None)

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

col1, col2 = st.columns(2, gap="large")
with col1:
    st.subheader("Weekly speed")
    st.dataframe(round(summary_df,2))

with col2:
    st.subheader("Survey speed")
    st.dataframe(round(survey_average,2))

