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
 
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
city = load_lottiefile("Lotties/city.json") 

st.title('Electrifying Connecticut')

st.markdown('## Project Description')
st.markdown('For our final project we were given freedom when choosing both the topic and the assingement.') 
             
st.markdown('In this project I decided to create an app encouraging the people from Connecticut to buy electric cars.')

project_contents = """Project contents:
\n
1. ETL: Extract, Transform, and Load.
\n
2. Database: The database I created for the extracted data.
\n
3. App:
   - Streamlit code
   - Analysis
\n
\n
4. Predictive Model: A model created to predict the future population of electric cars.

"""

selected_option = st.selectbox('Choose from contents:', ('ETL', 'DataBase', 'App: -Finder', 'App: -Analysis', 'Predictive model'))
st.info(project_contents)
st_lottie(
city,
speed=1,
reverse=False,
loop=True,
)

