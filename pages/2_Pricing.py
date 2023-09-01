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
price = pd.read_csv('Cars_Price_Clean.csv')
Prices, Models, Makes = st.columns(3)
disable_Make = st.checkbox("Disable Make Filter", value = True)
disable_Price = st.checkbox("Disable Price Filter")
disable_Model = st.checkbox("Disable Model Filter", value = True)
if not disable_Model:
    with st.expander("Filter by Model"):
        model = st.selectbox('Select a Model', price.model.unique())
if not disable_Make:
    with st.expander("Filter by Make"):
        make = st.selectbox('Select a Make', price.Make.unique())
if not disable_Price:
    with st.expander("Filter by Price"):
        price_min, price_max = st.select_slider('Select a Price Range', 
                                                options=[i for i in range(0, price.price.max() + 1)],
                                                value=[0, price.price.max()], key="price")
if not disable_Make and not disable_Price and not disable_Model:
    var = price[(price.model == model) &
                (price.price >= price_min) &
                (price.price <= price_max) &
                (price.Make == make)]
elif not disable_Make and not disable_Price:
    var = price[(price.price >= price_min) &
                (price.price <= price_max) &
                (price.Make == make)]
elif not disable_Make and not disable_Model:
    var = price[(price.model == model) &
                (price.Make == make)]
elif not disable_Price and not disable_Model:
    var = price[(price.model == model) &
                (price.price >= price_min) &
                (price.price <= price_max)]
elif not disable_Make:
    var = price[(price.Make == make)]
elif not disable_Price:
    var = price[(price.price >= price_min) &
                (price.price <= price_max)]
elif not disable_Model:
    var = price[(price.model == model)]
else:
    var = price
st.dataframe(var)