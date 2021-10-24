# pip install streamlit
import streamlit as st
from model import predict_duration
import numpy as np

st.set_page_config(page_title="Seoul Bike Trip Duration Prediction App",
                   page_icon="🛴", layout="wide")


with st.form("prediction_form"):

    st.header("Enter the significant values:")

    distance = st.number_input("Distance: ", value=0, format="%d")
    haversine = st.number_input("Haversine: ")
    pmonth=st.slider("Pickup Month: ",  min_value=1, max_value=12)
    pday=st.slider("Pickup Day: ",  min_value=1, max_value=31)
    phour = st.slider("Pickup Hour: ", 0, 23, value=0, format="%d")
    pmin = st.slider("Pickup Minute: ", 0, 59, value=0, format="%d")
    pdweek=st.slider("Pickup Week: ",  min_value=0, max_value=6)
    dmonth=st.slider("Drop Month: ",  min_value=1, max_value=12)
    dday=st.slider("Drop Day: ",  min_value=1, max_value=31)
    dhour = st.slider("Dropoff Hour: ", 0, 23, value=0, format="%d")
    dmin = st.slider("Dropoff Minute: ", 0, 59, value=0, format="%d")
    ddweek=st.slider("Drop Week: ",  min_value=0, max_value=6)
    temp = st.number_input("Temp: ")
    precip=st.number_input("Precipitation: ")
    wind=st.number_input("wind: ")
    humid = st.number_input("Humid: ")
    solar = st.number_input("Solar: ")
    snow=st.number_input("Snow: ")
    groundtemp=st.number_input("GroundTemp: ")
    dust = st.number_input("Dust: ")

    submit_val = st.form_submit_button("Predict Duration")

if submit_val:
    # If submit is pressed == True
    attribute = [distance, haversine,pmonth,pday, phour,pmin,pdweek,dmonth,dday, dhour,dmin,ddweek, temp,precip, wind, humid, solar,snow,groundtemp, dust]


    if attribute.shape == (1,20):
        print("attributes valid")
        

    value = predict_duration(attributes= attribute)


    st.header("Here are the results:")
    st.success(f"The Duration predicted is {value} mins")