import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
df = pd.read_csv('India.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

info = list(df.columns[6:])

st.sidebar.title('Indian census 2011')

state = st.sidebar.selectbox('Select a state', list_of_states)

primary = st.sidebar.selectbox('Select the primary Parameter', info)
secondary = st.sidebar.selectbox('Select the secondary Parameter', info)

plot = st.sidebar.button('Plot')

if plot:
    if state == 'Overall India':
        st.title('Overall India')
        st.text('Size represents primary parameter')
        st.text('Color represents sexondary parameter')
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", zoom=4, size=primary, color=secondary, size_max=35,
                                color_continuous_scale=px.colors.cyclical.IceFire, mapbox_style='carto-positron',
                                height=700, width=1200, hover_name='District')
        st.plotly_chart(fig)
    else:
        state_df = df[df['State'] == state]
        st.text('Size represents primary parameter')
        st.text('Color represents sexondary parameter')
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", zoom=6, size=primary, color=secondary, size_max=35,
                                color_continuous_scale=px.colors.cyclical.IceFire, mapbox_style='carto-positron',
                                height=700, width=1200, hover_name='District')
        st.plotly_chart(fig)
