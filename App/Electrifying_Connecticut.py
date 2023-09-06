import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import json
from streamlit_lottie import st_lottie
import requests
st.title('Electrifying Connecticut') 
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
st.markdown('## Project Description')


    

city = load_lottiefile("Lotties/city.json")  # replace link to local lottie file


st_lottie(
    city,
    speed=1,
    reverse=False,
    loop=True,
)