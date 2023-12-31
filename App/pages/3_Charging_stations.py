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
import streamlit.components.v1 as components
st.title('Charging Stations')

st.divider()


selec= st.sidebar.selectbox(
        'Choose BI Tool',
        ('Python',
         'Tableau'),
        placeholder = 'Python')
if selec == 'Python':
    stations = pd.read_csv('../Data/Clean_Charging_stations.csv')
    st.warning('There are more than 340 Charging Stations across Connecticut, find out which one is the closest to you!')

    m = folium.Map(location= [ 41.730405,-72.790618 ], tiles = 'OpenStreetMap', zoom_start = 10)

    for i,row in stations.iterrows():
        latitude = stations.at[i, 'latitude']
        longitude = stations.at[i, 'longitude']
        name = stations.at[i, 'street_address']
        evse= stations.at[i, 'evse_units']
        folium.Marker(location= [longitude, latitude],popup=[f'Adress: {name}', f"Units: {evse}"],icon= folium.Icon(color='green', icon = 'plug',             prefix='fa')).add_to(m)
    st_data = st_folium(m, width=725)
    st.info('The map above showcases the location of the charging stations with their respective Name, adress and number of EVSE Units (The number of charging points within the station).')
    
if selec == 'Tableau':
    st.warning('There are more than 340 Charging Stations across Connecticut, find out which one is the closest to you!')
    components.html("<div class='tableauPlaceholder' id='viz1694107809274' style='position: relative'><noscript><a href='#'><img alt='Dashboard 14 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Li&#47;Libro1_16917526419450&#47;Dashboard14&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Libro1_16917526419450&#47;Dashboard14' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Li&#47;Libro1_16917526419450&#47;Dashboard14&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1694107809274');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='800px';vizElement.style.minHeight='747px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='800px';vizElement.style.minHeight='747px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>",height= 520)
    st.info('The map above showcases the location of the charging stations with their respective Name, adress and number of EVSE Units (The number of charging points within the station).')