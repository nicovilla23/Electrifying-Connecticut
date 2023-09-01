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

st.title('Electrifying Connecticut') 

cars = pd.read_csv('Clean_Electric_Vehicle_Population_Data.csv')
price = pd.read_csv('Cars_Price_Clean.csv')
stations = pd.read_csv('Clean_Charging_stations.csv')











CAFVs, Electric_Ranges, Years, Makes = st.columns(4)
with Makes:
    Make= st.selectbox('Filter by Make' , cars.make.unique())
with CAFVs:
    CAFV = st.selectbox('Filter by CAFV', cars.cafv_eligibilaty.unique())
with Years:
    year_min, year_max = st.select_slider('Filter by Years', 
                                        options=[i for i in range(0,cars.model_year.max()+1)],
                                        value=[0, cars.model_year.max()])
with Electric_Ranges:
    electric_range_min, electric_range_max = st.select_slider('Filter by Electric Range', 
                                        options=[i for i in range(0,cars.electric_range.max()+1)],
                                        value=[0, cars.electric_range.max()])
df1 = cars[['model_year','make', 'model', 'cafv_eligibilaty','electric_range','electric_vehicle_type']].sort_values(by='model_year')   
var = df1[(df1.cafv_eligibilaty == CAFV) &
              (df1.model_year >= year_min) &
              (df1.model_year <= year_max) &
              
              (df1.electric_range >= electric_range_min) &
              (df1.electric_range <= electric_range_max) &
              (df1.make == Make)].drop_duplicates().reset_index(drop=True)


st.dataframe(var)
df_plot = df1[(df1.cafv_eligibilaty == CAFV) &
              (df1.model_year >= year_min) &
              (df1.model_year <= year_max) &
              
              (df1.electric_range >= electric_range_min) &
              (df1.electric_range <= electric_range_max) &
              (df1.make == Make)]

color_map = {
    'Electric': 'blue',
    'Hybrid': 'green',
    'Plug-in Hybrid': 'orange'
}
colors = [color_map.get(type, 'gray') for type in df_plot['electric_vehicle_type']]

fig, ax = plt.subplots()
plt.title('Models by year and type with their electric range ')
labels = df_plot['model'] + ' - ' + df_plot['model_year'].astype(str)
ax.barh(y=labels, width=df_plot['electric_range'], color=colors)
legend_elements = [plt.Rectangle((0, 0), 1, 1, color=color) for color in color_map.values()]
labels_legend = color_map.keys()
ax.legend(legend_elements, labels_legend)
st.pyplot(fig)