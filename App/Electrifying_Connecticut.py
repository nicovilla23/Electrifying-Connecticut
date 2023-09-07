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

st.divider()
st.markdown('## Project Description')
st.markdown('For our final project we were given freedom when choosing both the topic and the assingement.') 
             
st.markdown('In this project I decided to create an app encouraging the people from Connecticut to buy electric cars.')


selected_option = st.selectbox('Choose from contents:', ('ETL', 'DataBase', 'App: -Finder', 'App: -Analysis', 'Predictive model'))
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
st.info(project_contents)
if selected_option == 'ETL':
    st.subheader('ETL')
    e = '''The first step in the project was to define a theme and an objective , the next one was to find the data from where to work with (Extraction).
\n 
During this project I extracted 4 different datasets, 2 of them were downloaded and the other 2 were obtained using scrapping techniques such as 'get' and 'BeautifulSoup'. '''
    st.info(e)
    st.image('../../Images/Captura de Pantalla 2023-09-07 a las 20.36.02')
    t = ''' After extracting the data I need to Transform it, which entails using python libraries, in this case Pandas, to alter the data so that it is easier to work with and fits the objectives we are looking for.'''
    st.info(t)
    st.image('../Images/Captura de Pantalla 2023-09-07 a las 20.37.00')
    l = ''' The last step of the ETL is Loading, in which I uploaded the clean data to a database I had previously created.'''
    st.info(l)
    st.image('../Images/Captura de Pantalla 2023-09-07 a las 20.40.25')
    
if selected_option == 'DataBase':
    database= ''' This is the usable database I created for the project.'''
    st.info(database)
    st.image('../Images/Captura de Pantalla 2023-09-07 a las 20.45.05')
if selected_option == 'App: -Finder':
    
    finder= ''' The Finder was created by mixing different Python libraries such as Streamlit, Pandas and Folium to make an interactive, filterable finder so that the user can search for a more suitable option.'''
    st.info(finder)
    st.image('../Images/Captura de Pantalla 2023-09-07 a las 20.46.07')
if selected_option== 'App: -Analysis':
    analysis = ''' In the Analysis, via critical thinking I obtained insight about the cars and displayed in the form of metric and graphics.
\n
Each Analysis has two sections, Python and Tableau. 
\n 
 - The python section was made using a library called plost in which i can showcase the previously discovered insight by coding it manually.
\n
 - The Tableau section has some graphics which were integrated to the App by html components from the on-line tableau public and where created using tableau desktop.'''
    st.info(analysis)
    co1,co2= st.columns(2)
    with co1:
        st.image('../Images/Captura de Pantalla 2023-09-07 a las 20.47.34')
    with co2:
        st.image('../Images/Captura de Pantalla 2023-09-07 a las 20.49.20')
if selecte_option== 'Predictive model':
    predictive= ''' For the predictive model the first step was to scrap and transform a dataset containing previous registers of the population of electric cars. In the next step I trained a polynomial regression model using the clean dataset. To finalise I predicted the population for the next years using the model and plotted them using the plost library.'''
    st.info(predictive)
    st.image('../Images/Captura de Pantalla 2023-09-07 a las 20.50.03')
    

    
st_lottie(
city,
speed=1,
reverse=False,
loop=True,
)


