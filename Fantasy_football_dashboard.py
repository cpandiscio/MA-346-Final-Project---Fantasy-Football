import pandas as pd
import streamlit as st
import altair as alt

df1 = pd.read_csv('final_football_data.csv')

st.title("Fantasy Football Data")
st.sidebar.header("User Inputs for Graph")

st.write(df1)

# Filters UI
subset_data = df1
fantasy_name_input = st.sidebar.multiselect(
'Player',
df1.groupby('Player').count().reset_index()['Player'].tolist())
# by player name
if len(fantasy_name_input) > 0:
    subset_data = df1[df1['Player'].isin(fantasy_name_input)]

## Bar Chart

st.subheader('Players Touchdown Performance')
total_player_TD_graph  =alt.Chart(subset_data).transform_filter(
   alt.datum.TotalTD > 0
).mark_bar().encode(
    x=alt.X('Player', type='nominal', title='Player'),
    y=alt.Y('sum(TotalTD):Q',  title='Total Touchdown'),
    color='Player',
    tooltip = 'sum(TotalTD)',
).properties(
    width=1500,
    height=600
).configure_axis(
    labelFontSize=17,
    titleFontSize=20
)

st.altair_chart(total_player_TD_graph)