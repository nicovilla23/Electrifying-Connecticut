import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import folium
from folium.plugins import MarkerCluster
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium

st.title('Electrifying Connecticut') 


stations = pd.read_csv('Clean_Charging_stations.csv')

m = folium.Map(location= [ 41.730405,-72.790618 ], tiles = 'OpenStreetMap', zoom_start = 10)

for i,row in stations.iterrows():
    latitude = stations.at[i, 'latitude']
    longitude = stations.at[i, 'longitude']
    name = stations.at[i, 'street_address']
    evse= stations.at[i, 'evse_units']
    folium.Marker(location= [longitude, latitude],popup=[f'Adress: {name}', f"Units: {evse}"],icon= folium.Icon(color='green', icon = 'plug',             prefix='fa')).add_to(m)
st_data = st_folium(m, width=725)