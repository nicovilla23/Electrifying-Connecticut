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

st.title('Finding your Car') 

cars = pd.read_csv('../Data/Clean_Electric_Vehicle_Population_Data.csv')
price = pd.read_csv('../Data/Cars_Price_Clean.csv')
stations = pd.read_csv('../Data/Clean_Charging_stations.csv')




st.divider()
st.info('In this page you will able to filter through different specifications such as Electric range or Make to find the one that fits you best!')




CAFVs, Makes = st.columns(2)
with Makes:
    Make= st.selectbox('Filter by Make' , cars.make.unique())
with CAFVs:
    CAFV = st.selectbox('Filter by CAFV', cars.cafv_eligibilaty.unique())

c1,c2 = st.columns(2)
with c1:
    year_min, year_max = st.select_slider('Filter by Years', 
                                        options=[i for i in range(1997,cars.model_year.max()+1)],
                                        value=[1997, cars.model_year.max()], key='Years')
with c2:
    electric_range_min, electric_range_max = st.select_slider('Filter by Electric Range', 
                                        options=[i for i in range(0,cars.electric_range.max()+1)],
                                        value=[0, cars.electric_range.max()], key="ER")
st.info('Click on the sliders and the selectors above to alter the table below')
st.divider()
df1 = cars[['model_year','make', 'model', 'cafv_eligibilaty','electric_range','electric_vehicle_type']].sort_values(by='model_year')   
var = df1[(df1.cafv_eligibilaty == CAFV) &
              (df1.model_year >= year_min) &
              (df1.model_year <= year_max) &
              
              (df1.electric_range >= electric_range_min) &
              (df1.electric_range <= electric_range_max) &
              (df1.make == Make)].drop_duplicates().reset_index(drop=True)


st.dataframe(var, hide_index=True)
st.divider()
df_plot = df1[(df1.cafv_eligibilaty == CAFV) &
              (df1.model_year >= year_min) &
              (df1.model_year <= year_max) &
              
              (df1.electric_range >= electric_range_min) &
              (df1.electric_range <= electric_range_max) &
              (df1.make == Make)]

color_map = {
    'Electric': 'turquoise',
    'Hybrid': 'teal',
    'Plug-in Hybrid': (152/255, 251/255, 152/255)
}
colors = [color_map.get(type, 'gray') for type in df_plot['electric_vehicle_type']]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Models by Year and Type with their Electric Range', fontsize=16)
labels = df_plot['model'] + ' - ' + df_plot['model_year'].astype(str)
ax.barh(y=labels, width=df_plot['electric_range'], color=colors)


legend_elements = [plt.Rectangle((0, 0), 1, 1, color=color) for color in color_map.values()]
labels_legend = color_map.keys()
ax.legend(legend_elements, labels_legend, loc='lower right', fontsize=12)

ax.set_xlabel('Electric Range', fontsize=12)
ax.set_ylabel('Model - Year', fontsize=12)
ax.grid(axis='x', linestyle='--')

plt.tight_layout()
st.pyplot(fig)