import pandas as pd
import streamlit as st
import plotting 
import forecasting_utilities  as fu



HOME_AIRPORTS = ('LGW', 'LIS', 'LYS')
PAIRED_AIRPORTS = ('FUE', 'AMS', 'ORY')

df = pd.read_parquet('./data/traffic_10lines.parquet')

st.title('Traffic Forecaster')

with st.sidebar:
    home_airport = st.selectbox(
        'Home Airport', HOME_AIRPORTS)
    paired_airport = st.selectbox(
        'Paired Airport', PAIRED_AIRPORTS)
    forecast_date = st.date_input('Forecast Start Date')
    nb_days = st.slider('Days of forecast', 7, 30, 1)
    run_forecast = st.button('Forecast')
    

st.write('Home Airport selected:', home_airport)
st.write('Paired Airport selected:', paired_airport)
st.write('Days of forecast:', nb_days)
st.write('Date selected:', forecast_date)


# Affichage de la table

st.markdown('# Table des vols, pour la destination choisie, avec le nombre de passager total par jour')
st.dataframe(fu.generate_route_df(df,home_airport,paired_airport), width=600, height=300)

st.plotly_chart(plotting.draw_ts_multiple(fu.generate_route_df(df,home_airport,paired_airport), 'pax_total', covid_zone=True,display=False))
st.plotly_chart(plotting.draw_ts_multiple(fu.forecast_data(df,home_airport,paired_airport,nb_days), 'pax_total', covid_zone=True,display=False))
