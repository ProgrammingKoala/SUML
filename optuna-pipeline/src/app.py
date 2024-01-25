import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Prediction of Car Prices",
    #layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Prediction of Car Prices. Application created as a part of the project for *SUML*. Created by Jagoda Furmańczyk s22409, Thanondrak Arunsangsirinak s22130, Dawid Kazubski s22722"
    }
)

df = pd.read_csv("../data/01_raw/CarPrice.csv")

st.write(df)

st.divider()


st.write("Jagoda Furmańczyk s22409    Dawid Kazubski s22722    Thanondrak Arunsangsirinak s22130")

col1, mid, col2 = st.columns([1,1,20])
with col1:
    st.image('https://kartkaplus.pl/140-large_default/polsko-japonska-akademia-technik-komputerowych-naklejka-na-legitymacje-studencka.jpg', width=100)
with col2:
    st.title('Prediction of Car Prices')

st.divider()

st.slider("Estimators", 50, 300)
st.slider("Max Depth", 10, 50)
st.slider("Min Samples Split", 2, 32)
st.slider("Min Samples Leaf", 1, 32)

st.divider()

car = st.selectbox('Car:', (df['CarName'].unique()))
fuelType = st.selectbox('Fuel type:', (df['fueltype'].unique()))
aspiration = st.selectbox('Aspiration:', (df['aspiration'].unique()))
doornumber = st.selectbox('Number of doors:', (df['doornumber'].unique()))
carbody = st.selectbox('Car body:', (df['carbody'].unique()))
drivewheel = st.selectbox('Drivewheel:', (df['drivewheel'].unique()))
enginelocation = 'front'
wheelbase = st.selectbox('Wheel base:', (df['wheelbase'].unique()))
carlength = st.selectbox('Length of the car:', (df['carlength'].unique()))
#st.selectbox('', (df[''].unique()))

