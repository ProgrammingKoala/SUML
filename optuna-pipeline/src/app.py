import streamlit as st
import pandas as pd
import numpy as np
import time

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

# --- WEB PAGE CONFIGURATION
st.set_page_config(
    page_title="Prediction of Car Prices",
    #layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Prediction of Car Prices. Application created as a part of the project for *SUML*. Created by Jagoda Furmańczyk s22409, Thanondrak Arunsangsirinak s22130, Dawid Kazubski s22722"
    }
)

# --- LOADING OF DATA
df = pd.read_csv("../data/01_raw/CarPrice.csv")

# --- DYSPLAING DATA WHEN CHECKBOX IS TICKED
csv = convert_df(df)

show_table = st.checkbox("Show raw data", key="disabled")

if show_table:
    st.write(df)
    st.download_button(label="Download data as CSV",data=csv,file_name='CarPrice.csv',mime='text/csv')

st.divider()

# --- 'MAIN PAGE' code
st.write("Jagoda Furmańczyk s22409, Dawid Kazubski s22722, Thanondrak Arunsangsirinak s22130")
st.image('https://lh3.googleusercontent.com/proxy/Z1RdJVwT2tVCHUZwMfocw4Hv0HFT4x3p6TgeTeStNTwNTMGRkJsKt_kR9MfqBY5WKI0E9aGGE2GFDyZGfCZ3Xk7mxAT1IjBp_Cn3')
st.title('Prediction of Car Prices')

st.divider()

# --- SLIDERS
estimators = st.slider("Estimators", 50, 300)
max_depth = st.slider("Max Depth", 10, 50)
min_samples_split = st.slider("Min Samples Split", 2, 32)
min_samples_leaf = st.slider("Min Samples Leaf", 1, 32)

st.divider()

# --- SELECTBOXES FOR PARAMETERS NEEDED FOR PREDICTION
fuelType = st.selectbox('Fuel type:', (df['fueltype'].unique()))
carbody = st.selectbox('Car body:', (df['carbody'].unique()))
drivewheel = st.selectbox('Drivewheel:', (df['drivewheel'].unique()))
wheelbase = st.selectbox('Wheel base:', sorted((df['wheelbase'].unique())))
carlength = st.selectbox('Length of the car:', sorted((df['carlength'].unique())), help='in inches')
carwidth = st.selectbox('Width of the car:', sorted((df['carwidth'].unique())), help='in inches')
carheight = st.selectbox('Height of the car:', sorted((df['carheight'].unique())), help='in inches')
curbweight = st.selectbox('Weight of the curb:', sorted((df['curbweight'].unique())))
enginesize = st.selectbox('Size of engine', sorted((df['enginesize'].unique())))
cylindernumber = st.selectbox('Number of cylinders', (df['cylindernumber'].unique()))
boreratio = st.selectbox('Bore ratio:', sorted((df['boreratio'].unique())))
stroke = st.selectbox('Stroke:', sorted((df['stroke'].unique())))
compressionratio = st.selectbox('Compression ratio', sorted((df['compressionratio'].unique())), help='The compression ratio is defined as the ratio between the volume of the cylinder with the piston in the bottom position, Vbottom (largest volume), and in the top position, Vtop (smallest volume).')
horsepower = st.selectbox('Horsepower:', sorted((df['horsepower'].unique())))
peakrpm =  st.selectbox('Peak RPM:', sorted((df['peakrpm'].unique())), help='Revolutions per minute.')
citympg = st.selectbox('City MPG:', sorted((df['citympg'].unique())), help='*City MPG:* the score a car will get on average in city conditions, with stopping and starting at lower speeds.')
highwaympg = st.selectbox('Highway MPG:', sorted((df['highwaympg'].unique())), help='*Highway MPG:* the average a car will get while driving on an open stretch of road without stopping or starting, typically at a higher speed.')

# -- MAKING PREDICTION 
if st.button('Make prediction'):
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.divider()
    st.success('Done!' + str(estimators))
    #dfp = pd.DataFrame(fuelType, carbody, drivewheel)
    #dfp.to_csv('predictionData')
    

# --- Not used but maybe used in future ---
# --- !!! DELETE BEFORE TURNING IN !!!  ---
#st.selectbox('', (df[''].unique()))   
#car = st.selectbox('Car:', (df['CarName'].unique()))
#aspiration = st.selectbox('Aspiration:', (df['aspiration'].unique()))
#doornumber = st.selectbox('Number of doors:', (df['doornumber'].unique()))
#enginelocation = 'front'