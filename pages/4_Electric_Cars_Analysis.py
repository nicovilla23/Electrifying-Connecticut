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
import matplotlib.pyplot as plt
import squarify

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
    ('Electric vs Plug-in Hybrids',
     'Electric Car Tendencies',
     'Prices per make',
     'Electric Range Tendency',
     'Most popular models',
     'Clean Alternative Fuel Vehicle Eligibility'))
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
    P_LY= len(cars[(cars['model_year']<= 2022) & (cars['model_year'] >= 2021) & (cars['electric_vehicle_type']== 'Plug-in Hybrid')]) 
    
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
    chart = plost.bar_chart(
    data=summary,
    bar='Make',
    value=['mean_price', 'min_price', 'max_price'],
    group=True)
if add_selectbox == 'Most popular models':    
    coln1, coln2 = st.columns((3,7))

    with coln1:
        copium = st.selectbox('Select model', cars.model.unique())

    with coln2:
        if copium in cars['model'].unique():
            st.metric(label='CAFV', value=cars.loc[cars['model'] == copium, 'cafv_eligibilaty'].values[0])

    coln3, coln4, coln5 = st.columns(3)

    with coln3:
        if copium in cars['model'].unique():
            st.metric(label='Electric Range', value=f"{cars.loc[cars['model'] == copium, 'electric_range'].values[0]} miles")

    with coln4:
        if copium in cars['model'].unique():
            st.metric(label='Make', value=cars.loc[cars['model'] == copium, 'make'].values[0])

    with coln5:
        if copium in cars['model'].unique():
            st.metric(label='Type', value=cars.loc[cars['model'] == copium, 'electric_vehicle_type'].values[0])
        lep = cars.groupby('model')['city'].count()
    lop = pd.DataFrame({'labels':lep.index,'size': lep.values})
    fig = px.treemap(lop, path=['labels'], values='size')
    fig.update_layout(
    width=800,  
    height=600,
    title='Most Popular Models')
    st.plotly_chart(fig)
if add_selectbox == 'Electric Range Tendency':
    co1, co2, co3, co4 = st.columns(4)
    E_11= cars[(cars['model_year']== 2011) & (cars['electric_vehicle_type']== 'Electric')]['electric_range'].mean()
    E_De = cars[(cars['model_year']== 2020) & (cars['electric_vehicle_type']== 'Electric')]['electric_range'].mean()
    P_11=cars[(cars['model_year']== 2011) & (cars['electric_vehicle_type']== 'Plug-in Hybrid')]['electric_range'].mean()
    P_De= cars[(cars['model_year']== 2020) & (cars['electric_vehicle_type']== 'Plug-in Hybrid')]['electric_range'].mean()  
    with co1:
        st.markdown('#### Electric')
        st.metric(label = 'In 2011', value = f'{(E_11):.2f} mi')
    with co2:
        st.markdown('#### Electric')
        st.metric(label = 'in 2020', value = f'{(E_De):.2f} mi' , delta = f' {((E_De/E_11) * 100):.2f}%')
    with co3:
        st.markdown('#### Plug-in Hybrid')
        st.metric(label = 'In 2011', value = f'{(P_11):.2f} mi' )
    with co4:
        st.markdown('#### Plug-in Hybrid')
        st.metric(label = 'in 2020', value = f'{(P_De):.2f} mi', delta = f' -27,18%')
    
    c1, c2, c3, c4 = st.columns(4)
    E_19= cars[(cars['model_year']== 2019) & (cars['electric_vehicle_type']== 'Electric')]['electric_range'].mean()
    E_Ly = cars[(cars['model_year']== 2020) & (cars['electric_vehicle_type']== 'Electric')]['electric_range'].mean()
    P_19=cars[(cars['model_year']== 2019) & (cars['electric_vehicle_type']== 'Plug-in Hybrid')]['electric_range'].mean()
    P_Ly= cars[(cars['model_year']== 2020) & (cars['electric_vehicle_type']== 'Plug-in Hybrid')]['electric_range'].mean()
    
    with c1:
        
        st.metric(label = 'In 2019', value = f'{(E_19):.2f} mi')
    with c2:
        
        st.metric(label = 'in 2020', value =f'{(E_Ly):.2f} mi' , delta = f' 21,39%')
    with c3:
        
        st.metric(label = 'In 2019', value = f'{(P_19):.2f} mi' )
    with c4:
        
        st.metric(label = 'in 2020', value =f'{(P_Ly):.2f} mi', delta = f' - 11,23%')
    
    lep = cars[(cars['model_year']>= 2011) & (cars['model_year']<= 2020)]
    pep = lep.groupby(['model_year', 'electric_vehicle_type'])['electric_range'].mean().reset_index()
    st.markdown('### Area Chart')
    plost.area_chart(data=pep, x='model_year', y='electric_range', color='electric_vehicle_type', width=800, height=500 , title='Electric Range Tendency per Type')
if add_selectbox == 'Clean Alternative Fuel Vehicle Eligibility':
    
    no_unk = cars[cars['cafv_eligibilaty'] != 'Eligibility unknown as battery range has not been researched']
    cafv_count = no_unk['cafv_eligibilaty'].value_counts()
    d_cafv = pd.DataFrame({'cafv': cafv_count.index, 'count': cafv_count.values})
    st.markdown('### Metrics')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label='CAFV Eligible', value= 18726 )
    with col2:
        st.metric(label="CAFV Eligible", value="67,36%")
    with col3:
        st.metric(label="CAFV Not Eligible", value=9072 )
    with col4:
        st.metric(label="CAFV Not Eligible", value="32,64%")
    c1, c2 = st.columns((6,4))
    with c1:
        st.markdown('### Bar Plot')
        plost.bar_chart(data= d_cafv, bar= 'cafv', value= 'count', color = 'count',height= 500,use_container_width = True)

    with c2:
        st.markdown('### Donut Chart')
        plost.donut_chart(data= d_cafv,theta='count' ,color = 'cafv' ,legend= 'bottom', use_container_width = True)
    plost.scatter_chart(
    data=cars,
    x='cafv_eligibilaty',
    y='electric_range')


    
    
    
    



