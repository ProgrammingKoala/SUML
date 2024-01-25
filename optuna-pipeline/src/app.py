import streamlit as st
import pandas as pd
import numpy as np
import time
import pickle



@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def create_array_gas(gasType):
    if gasType == 'gas':
        x = [1]
        return x
    else:
        x = []
        return x

def create_array_carbody(carbody):
    if carbody == 'hardtop':
        x = [1,0,0,0]
        return x
    elif carbody == 'hatchback':
        x = [0,1,0,0]
        return x
    elif carbody == 'sedan':
        x = [0,0,1,0]
        return x
    elif carbody == 'wagon':
        x = [0,0,0,1]
        return x
    else:
        x = [0,0,0,0]
        return x
    
def create_array_drivewheel(drivewheel):
    if carbody == 'fwd':
        x = [1,0]
        return x
    elif carbody == 'rwd':
        x = [0,1]
        return x
    else:
        x = [0,0]
        return x
    
def create_array_cilindernumber(carbody):
    if carbody == 'five':
        x = [1,0,0,0,0,0]
        return x
    elif carbody == 'four':
        x = [0,1,0,0,0,0]
        return x
    elif carbody == 'six':
        x = [0,0,1,0,0,0]
        return x
    elif carbody == 'three':
        x = [0,0,0,1,0,0]
        return x
    elif carbody == 'twelve':
        x = [0,0,0,0,1,0]
        return x
    elif carbody == 'two':
        x = [0,0,0,0,0,1]
        return x
    else:
        x = [0,0,0,0,0,0]
        return x

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
        #CREATIN ARRAYS FROM USER INPUT FOR MODEL
        array_gas = create_array_gas(fuelType)
        array_carbody = create_array_carbody(carbody)
        array_drivewheel = create_array_drivewheel(drivewheel)
        array_cylindernumber = create_array_cilindernumber(cylindernumber)
        
        #ADDING THE CREATED ARRAYS TOGETHER
        array_user_input = [wheelbase, carlength, carwidth, carheight, curbweight, enginesize, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg]
        final_array_user_input = [array_user_input + array_gas + array_carbody + array_drivewheel + array_cylindernumber]
        
        #PREDICTING THE CAR PRICE BASED ON MODEL
        pickled_model = pickle.load(open('../data/07_model_output/rfr_model.pickle', 'rb'))
        model_prediction = pickled_model.predict(final_array_user_input)

    st.divider() 
    st.success("Predicted price based on your input:  \n" + str(round(model_prediction[0], 3)) + "$")