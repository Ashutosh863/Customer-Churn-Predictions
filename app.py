import streamlit as st
import numpy as np
import pandas as pd
import joblib

pipeline = joblib.load('.venv\pipeline.pkl')

st.title("Customer Churn Prediction")
st.write("This app predicts whether a telecom customer is likely to churn based on their details ")

#user input
st.header("Enter Customer Details: ")

def user_input():
    tenure = st.slider("Tenure (Months)",0,72,12)
    monthly_charges = st.slider("Monthly Charges (s",18,120,30)
    total_charges = st.slider("Total Charges",18,9000,500)
    
# Binary input
    gender = st.selectbox("Gender",["Male","Female"])
    senior_citizen = st.selectbox("Senior Citizen",["No","Yes"])
    partner = st.selectbox("Partner",["No","Yes"])
    dependents = st.selectbox("Dependents",["no","Yes"])
    phone_service = st.selectbox("Phone Services",["No","Yes"])
    paperless_billing = st.selectbox("Paperless Billing",["No","Yes","No Internet Service"])
    online_security = st.selectbox("Online Security",["No","Yes","No Internet Service"])
    online_backup = st.selectbox("online backup",["No","Yes","No Internet Service"])
    device_protection = st.selectbox("device protection",["No","Yes","No Internet Service"])
    tech_support = st.selectbox("Tech Support",["No","Yes","No Internet Service"])
    streaming_tv = st.selectbox("Streaming TV",["No","Yes","No Internet Service"])
    streaming_movies = st.selectbox("Streaming Movies",["No","Yes","No Internet Service"])


# Categorical input
    contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])
    internet_service = st.selectbox("Internet Service",["DSL","opticr","Fiber","No"])
    payment_method = st.selectbox("Payment_Method",["Electronic Check","Mailes Check","Bank transfer (automatic)","Credit card (automatic)"])

    data = {
         "tenure":tenure,
         "monthly_charges":monthly_charges,
         "total_charges":total_charges,
         "gender":gender,
         "senior_citizen":senior_citizen,
         "partner":partner,
         "dependents":dependents,
         "phone_servic":phone_service,
         "paperless_billing":paperless_billing,
         "online_security":online_security,
         "online_backup":online_backup,
         "device_protection":device_protection,
         "tech_support":tech_support,
         "streaming_tv":streaming_tv,
         "streaming_movies":streaming_movies,
         "contract":contract,
         "internet_service":internet_service,
         "payment_method":payment_method
    }

    features = pd.DataFrame([data])
    return features

input_df = user_input()

#Prediction
if st.button("Predicte Churn"):
    prediction = pipeline.predict(input_df)
    prediction_proba = pipeline.predict_proba(input_df)[:,1]

    if prediction[0] ==1:
        st.error(f"The customer is like;y to churn: Probability {prediction_proba[0]*100:.2f}%")
    else:
        st.success(f"The customer is not likely to churn : Probability {prediction_proba[0]*100:.2f}%")
    
    #show input data
    if st.checkbox("Show Input Data"):
        st.write(input_df)