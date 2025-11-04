# --- IMPORT LIBRARIES ---
import streamlit as st          # main Streamlit library
import pandas as pd             # for data handling
import numpy as np              # for numerical operations
import pickle                   # to load your saved ML model

# --- LOAD MODEL ---
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

# --- APP TITLE ---
st.title("Heart Disease Risk Predictor")

# --- USER INPUT SLIDERS ---
st.header("Patient Information")

age = st.slider("Age", 20, 100, 50)                   # min, max, default
sex = st.selectbox("Sex", ["Male", "Female"])        # categorical
cp = st.slider("Chest Pain Type (0-3)", 0, 3, 0)
trestbps = st.slider("Resting Blood Pressure", 80, 200, 120)
chol = st.slider("Cholesterol", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
restecg = st.slider("Resting ECG (0-2)", 0, 2, 1)
thalach = st.slider("Max Heart Rate Achieved", 70, 210, 150)
exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)
slope = st.slider("Slope of ST Segment (0-2)", 0, 2, 1)
ca = st.slider("Number of Major Vessels (0-3)", 0, 3, 0)
thal = st.slider("Thalassemia (1-3)", 1, 3, 3)

# --- CONVERT INPUTS TO MODEL FORMAT ---
# encode categorical variables
sex_val = 1 if sex == "Male" else 0
fbs_val = 1 if fbs == "Yes" else 0
exang_val = 1 if exang == "Yes" else 0

# create input array
input_features = np.array([[age, sex_val, cp, trestbps, chol, fbs_val,
                            restecg, thalach, exang_val, oldpeak, slope, ca, thal]])

# --- PREDICTION BUTTON ---
if st.button("Predict Risk"):
    prediction = model.predict(input_features)[0]  # 0 or 1
    probability = model.predict_proba(input_features)[0][1]  # probability of 1

    if prediction == 1:
        st.warning(f"High risk of heart disease ({probability*100:.1f}% probability)")
    else:
        st.success(f"Low risk of heart disease ({probability*100:.1f}% probability)")
