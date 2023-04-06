import streamlit as st 
import pandas as pd
import pickle
import requests
from datetime import datetime
data_heart = pickle.load(open("X_heart.pkl","rb"))
data_diabetes= pickle.load(open("X_diabeties.pkl","rb"))

data_heart_log = pickle.load(open("logistic.pkl","rb"))
data_dibbetes_random = pickle.load(open("X_dieases_random.pkl","rb"))

with st.sidebar:
    select = st.selectbox("Multiple Disease Prediction System",
                         ["Diabetes Prediction",
                          "Heart Disease Prediction"],
                         index=0)

if(select == "Diabetes Prediction"):
    st.title("Diabetes Prediction")
    Pregnancies = st.number_input('Enter your Number of Pregnancies', min_value=0, max_value=12, value=0, step=1)
    Glucose = st.number_input('Enter your Glucose level', min_value=10, max_value=500, value=120, step=1)
    BloodPressure = st.number_input('Enter your Blood Pressure level', min_value=10, max_value=500, value=120, step=1)
    SkinThickness = st.number_input('Enter your Skin Thickness', min_value=0, max_value=50, value=12, step=1)
    Insulin = st.number_input('Enter your Insulin level', min_value=0, max_value=300, value=0, step=1)
    BMI = st.number_input('Enter your BMI', min_value=0, max_value=100, value=0, step=1)
    DiabetesPedigreeFunction = st.number_input('Enter your Diabetes Pedigree Function', min_value=0, max_value=100, value=0, step=1)
    age = st.number_input('Enter your age', min_value=0, max_value=120, value=30, key='age')
    
    input_list_diabetes = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, age]
    
    if st.button("Predict"):
        prediction_diabetes = data_dibbetes_random.predict([input_list_diabetes])
        
        if prediction_diabetes == 1:
            st.title("SORRY : Please SEE THE DOCTOR")
        else:
            st.title("You are Fine")
        

if(select == "Heart Disease Prediction"):
    st.title("Heart Disease Prediction")
    
    age = st.number_input('Enter your age', min_value=0, max_value=120, value=30, step=1)
    sex = st.number_input('Select your sex: 1 for Male, 2 for Female', min_value=1, max_value=2, value=1, step=1)
    cp = st.number_input('Enter your chest pain type (1-4)', min_value=1, max_value=4, value=1, step=1)
    trestbps = st.number_input('Enter your resting blood pressure', min_value=0, max_value=300, value=120, step=1)
    chol = st.number_input('Enter your serum cholesterol level', min_value=0, max_value=600, value=200, step=1)
    fbs = st.number_input('Enter your fasting blood sugar (1 = true, 0 = false)', min_value=0, max_value=1, value=0, step=1)
    restecg = st.number_input('Enter your resting electrocardiographic results (0-2)', min_value=0, max_value=2, value=0, step=1)
    thalach = st.number_input('Enter your maximum heart rate achieved', min_value=0, max_value=300, value=150, step=1)
    exang = st.number_input('Enter your exercise-induced angina (1 = yes, 0 = no)', min_value=0, max_value=1, value=0, step=1)
    oldpeak = st.number_input('Enter your ST depression induced by exercise relative to rest', min_value=0.0, max_value=10.0, value=0.0, step=0.1)
    slope = st.number_input('Enter the slope of the peak exercise ST segment (1-3)', min_value=1, max_value=3, value=1, step=1)
    ca = st.number_input('Enter the number of major vessels colored by fluoroscopy (0-4)', min_value=0, max_value=4, value=0, step=1)
    thal = st.number_input('Enter the thalassemia type (3 = normal, 6 = fixed defect, 7 = reversible defect)', min_value=3, max_value=7, value=3, step=1)

    # create a dictionary from the input values and convert it into a dataframe
    input_data = [age, sex, cp,  trestbps,chol,fbs,restecg,thalach, exang,  oldpeak, slope,  ca, thal]
    
    
    if st.button("Predict_heat",key="heart_disease_prediction"):
        prediction_heart = data_heart_log.predict([input_data])
        
        if prediction_heart == 1:
            st.title("SORRY : Please SEE THE DOCTOR")
        else:
            st.title("You are Fine")