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
 
 

st.title('Project Description')

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
    st.image('https://github.com/nicovilla23/Electrifying-Connecticut/blob/main/Images/Captura%20de%20Pantalla%202023-09-07%20a%20las%2020.36.02.png?raw=true')
    t = ''' After extracting the data I need to Transform it, which entails using python libraries, in this case Pandas, to alter the data so that it is easier to work with and fits the objectives we are looking for.'''
    st.info(t)
    st.image('https://github.com/nicovilla23/Electrifying-Connecticut/blob/main/Images/Captura%20de%20Pantalla%202023-09-07%20a%20las%2020.37.00.png?raw=true')
    l = ''' The last step of the ETL is Loading, in which I uploaded the clean data to a database I had previously created.'''
    st.info(l)
    st.image('https://github.com/nicovilla23/Electrifying-Connecticut/blob/main/Images/Captura%20de%20Pantalla%202023-09-07%20a%20las%2020.40.25.png?raw=true')
    
if selected_option == 'DataBase':
    st.subheader('DataBase')
    database= ''' This is the usable database I created for the project.'''
    st.info(database)
    st.image('https://github.com/nicovilla23/Electrifying-Connecticut/blob/main/Images/Captura%20de%20Pantalla%202023-09-07%20a%20las%2020.45.05.png?raw=true')
if selected_option == 'App: -Finder':
    st.subheader('App: -Finder')
    
    finder= ''' The Finder was created by mixing different Python libraries such as Streamlit, Pandas and Folium to make an interactive, filterable finder so that the user can search for a more suitable option.'''
    st.info(finder)
    st.image('https://github.com/nicovilla23/Electrifying-Connecticut/blob/main/Images/Captura%20de%20Pantalla%202023-09-07%20a%20las%2020.46.07.png?raw=true')
if selected_option== 'App: -Analysis':
    st.subheader('App: -Analysis')
    analysis = ''' In the Analysis, via critical thinking I obtained insight about the cars and displayed in the form of metric and graphics.
\n
Each Analysis has two sections, Python and Tableau. 
\n 
 - The python section was made using a library called plost in which i can showcase the previously discovered insight by coding it manually.
\n
 - The Tableau section has some graphics which were integrated to the App by html components from the on-line tableau public and where created using tableau desktop.'''
    st.info(analysis)
    
    
    st.image('https://github.com/nicovilla23/Electrifying-Connecticut/blob/main/Images/Captura%20de%20Pantalla%202023-09-07%20a%20las%2020.47.34.png?raw=true')

    st.image('https://github.com/nicovilla23/Electrifying-Connecticut/blob/main/Images/Captura%20de%20Pantalla%202023-09-07%20a%20las%2020.49.20.png?raw=true')
if selected_option== 'Predictive model':
    st.subheader('Predictive model')
    predictive= ''' For the predictive model the first step was to scrap and transform a dataset containing previous registers of the population of electric cars. In the next step I trained a polynomial regression model using the clean dataset. To finalise I predicted the population for the next years using the model and plotted them using the plost library.'''
    st.info(predictive)
    st.image('https://github.com/nicovilla23/Electrifying-Connecticut/blob/main/Images/Captura%20de%20Pantalla%202023-09-07%20a%20las%2020.50.03.png?raw=true')
    

    

