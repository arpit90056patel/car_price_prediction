import pandas as pd
import numpy as np
import datetime
import xgboost as xgb
import streamlit as st

def main():
    html_temp ="""<h1>Car Price Prediction</h1>"""
    model = xgb.XGBRegressor()
    model.load_model("xgb_model.json")

    st.markdown(html_temp,unsafe_allow_html=True )
    st.markdown("This app will help you to predict your car selling price" )

    p1 = st.number_input("Please enter ex-showroom price (In Lakhs)", 2.5,25.0,step=1.0)
    p2 = st.number_input("Please enter car driven (in kilometers)",100,500000,step=100)

    s1 = st.selectbox("Please select fuel type",["Petrol","Diesel","CNG"])
    if s1 == "Petrol":
        p3 = 0
    elif s1 == "Diesel":
        p3 = 1
    elif s1 == "CNG":
        p3 = 2

    s2 = st.selectbox("Please select transmission type",["Manual","Automatic"])
    if s2 == "Manual":
        p4 = 0
    elif s2 == "Automatic":
        p4 = 1

    s3 = st.selectbox("Please select owner type",["First Owner","Second Owner","Third Owner","Fourth & Above Owner"])
    if s3 == "First Owner":
        p5 = 0
    elif s3 == "Second Owner":
        p5 = 1
    elif s3 == "Third Owner":
        p5 = 2  
    elif s3 == "Fourth & Above Owner":
        p5 = 3  

    s4 = st.selectbox("Please select seller type",["Individual","Dealer"])
    if s4 == "Individual":
        p8 = 0   
    elif s4 == "Dealer":
        p8 = 1
    
    date_time = datetime.datetime.now()
    years = st.number_input("Car purchase year", 1900, date_time.year, step=1)
    p11 = date_time.year - years

    data_new = pd.DataFrame({
        'Present_Price': [p1],
        'Kms_Driven': [p2],
        'Fuel_Type': [p3],
        'Seller_Type': [p8],
        'Transmission': [p4],
        'Owner': [p5],
        'Age': [p11]
    }, index=[0])

    if st.button("Predict"):
        pred = model.predict(data_new)
        st.success("You can sell your car at {:.2f} lakhs".format(pred[0])) 

if __name__ == '__main__':
    main()
    