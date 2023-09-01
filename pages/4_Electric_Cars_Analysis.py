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
import plotly.express as px
import plost
st.title('Electrifying Connecticut') 
cars = pd.read_csv('Clean_Electric_Vehicle_Population_Data.csv')
price = pd.read_csv('Cars_Price_Clean.csv')
stations = pd.read_csv('Clean_Charging_stations.csv')

# Charting Types
counts = cars['electric_vehicle_type'].value_counts()
data = pd.DataFrame({'Type': counts.index, 'Count': counts.values})
# Charting tendency
t_counts= pd.DataFrame(cars.groupby('model_year')['electric_vehicle_type'].value_counts())


add_selectbox = st.sidebar.selectbox(
    "Choose the analysis",
    ('Electric vs Plug-in Hybrids'
     ,'Electric Car Tendencies',
    'Cars Registered by make',
    'Amount of models per make',
    'Prices per make',
    'Most popular models',
    'Electric Range Tendency'))
if add_selectbox == 'Electric vs Plug-in Hybrids':
            st.markdown('### Metrics')
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(label="Electric", value="21.723")
            with col2:
                st.metric(label="Electric", value="59,87%")
            with col3:
                st.metric(label="Plug-in Hybrid ", value="14.559")
            with col4:
                st.metric(label="Plug-in Hybrid ", value="40,12%")
            c1, c2 = st.columns((6,4))
            with c1:
                st.markdown('### Bar Plot')
                plost.bar_chart(data=data, bar='Type', value='Count', color = 'Type' ,height= 500,use_container_width = True)

            with c2:
                st.markdown('### Donut Chart')
                plost.donut_chart(data= data,theta='Count' ,color = 'Type' ,legend= 'bottom', use_container_width = True)
if add_selectbox == 'Electric Car Tendencies':
    st.markdown('### Metrics')
    colu1, colu2, colu3, colu4 = st.columns(4)
    E_12=len(cars[(cars['model_year']<= 2012) & (cars['electric_vehicle_type']== 'Electric')])
    E_DE = len(cars[(cars['model_year']<= 2022) & (cars['model_year'] >= 2010) & (cars['electric_vehicle_type']== 'Electric') ])
    P_12=len(cars[(cars['model_year']<= 2012) & (cars['electric_vehicle_type']== 'Plug-in Hybrid')])
    P_DE= len(cars[(cars['model_year']<= 2022) & (cars['model_year'] >= 2010) & (cars['electric_vehicle_type']== 'Plug-in Hybrid') ]) 
    with colu1:
        st.markdown('#### Electric')
        st.metric(label = 'In 2012', value = E_12)
    with colu2:
        st.markdown('#### Electric')
        st.metric(label = 'Last Decade', value =f' + {E_DE}' , delta = f' {((E_DE/E_12) * 100):.2f}%')
    with colu3:
        st.markdown('#### Plug-in Hybrid')
        st.metric(label = 'In 2012', value = P_12 )
    with colu4:
        st.markdown('#### Plug-in Hybrid')
        st.metric(label = 'Last Decade', value =f' + {P_DE}', delta = f' {((P_DE/P_12) * 100):.2f}%')
    
    colo1, colo2, colo3, colo4 = st.columns(4)
    E_21=len(cars[(cars['model_year']<= 2021) & (cars['electric_vehicle_type']== 'Electric')])
    E_LY = len(cars[(cars['model_year']<= 2022) & (cars['model_year'] >= 2021) & (cars['electric_vehicle_type']== 'Electric') ])
    P_21=len(cars[(cars['model_year']<= 2021) & (cars['electric_vehicle_type']== 'Plug-in Hybrid')])
    P_LY= len(cars[(cars['model_year']<= 2022) & (cars['model_year'] >= 2021) & (cars['electric_vehicle_type']== 'Plug-in Hybrid') ]) 
    
    with colo1:
        
        st.metric(label = 'In 2021', value = E_21)
    with colo2:
        
        st.metric(label = 'Last Year', value =f' + {E_LY}' , delta = f' {((E_LY/E_21) * 100):.2f}%')
    with colo3:
        
        st.metric(label = 'In 2021', value = P_21 )
    with colo4:
        
        st.metric(label = 'Last Year', value =f' + {P_LY}', delta = f' {((P_LY/P_21) * 100):.2f}%')
    
    
    lop= cars[(cars['model_year']<= 2022) & (cars['model_year'] >= 2008) ]
    data = lop.groupby(['model_year', 'electric_vehicle_type']).size().reset_index(name='Count')
    st.markdown('### Area Chart')
    plost.area_chart(data=data, x='model_year', y='Count', color='electric_vehicle_type')

    
    
if add_selectbox == 'Prices per make':
    st.markdown('### Metrics')
    colm1,colm2,colm3 = st.columns(3)
    with colm1:
        st.metric(label='Minimum Price', value = f'{(price.price.min()):.2f}$')
    with colm2:
        st.metric(label='Average Price', value = f'{(price.price.mean()):.2f}$')
    with colm3:
        st.metric(label='Maximum Price', value = f'{(price.price.max()):.2f}$')
    summary = price.groupby('Make').agg(mean_price=('price', 'mean'), min_price=('price', 'min'), max_price=('price', 'max')).reset_index()
    st.markdown('### Stacked Bar Chart')
    plost.bar_chart(
    data=summary,
    bar='Make',
    value=['mean_price', 'min_price', 'max_price'],
    group=True)

    

    

fig, ax = plt.subplots()
ax.bar(x=Companies[:10], height=values[:10])
plt.figure(figsize=(9,5))
plt.xlabel('Make')
plt.ylabel('Count')
st.pyplot(fig)        #plost.donut_chart(data= cars,theta='electric_vehicle_type' ,color =[len(cars[cars['electric_vehicle_type']=='Plug-in Hybrid']),len(cars[cars['electric_vehicle_type']=='Electric'])] ,legend= 'bottom', use_container_width = True)