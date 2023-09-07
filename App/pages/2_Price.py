import plost
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

st.title('Price') 
price = pd.read_csv('../Data/Cars_Price_Clean.csv')

Prices, Models, Makes = st.columns(3)
st.divider()

st.warning('In this page you will be able to find the cars that best fit you budget')
st.info('Click on the disable Filter boxes to be able to search by Make or model')
c1,c2,c3 = st.columns(3)
with c1:
    disable_Make = st.checkbox("Disable Make Filter", value = True)
with c2:

    disable_Price = st.checkbox("Disable Price Filter")
with c3:

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
st.dataframe(var, use_container_width=True, hide_index=True)
st.info('The price displayed above is in american dollars  $')