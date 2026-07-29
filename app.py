import streamlit as st 
import joblib 

model = joblib.load("diabetes_model.pkl")

st.set_page_config(
    page_title = "Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction System")

st.write(
    "Enter the patient's medical details below and click **Predict**."
)

st.sidebar.title("About")

st.sidebar.write("""
This application predicts whether a patient is likely
to have diabetes using a Machine Learning model.
 
Model Used:
-Random Forest

Developed by :
Mariselvam M"""
)

col1,col2 = st.columns(2)


with col1:
    pregnancies = st.number_input("Pregnancies")

    glucose = st.number_input("Glucose",min_value=0,max_value=300,value=100)

    blood_pressure = st.number_input("Blood Pressure")

    skin_thickness = st.number_input("Skin Thickness")

with col2:


    insulin = st.number_input("Insulin")

    bmi = st.number_input("BMI")

    dpf = st.number_input("Diabetes Pedigree Function")

    age = st.number_input("Age",min_value=1,max_value=120,value=30)


if st.button("Predict"):

    input_data = [[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age
    ]]

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    if prediction[0] == 1:

        confidence = probability[0][1] * 100
        st.error("⚠️ Prediction: Diabetic")
        st.write(f"Confidence: {confidence:.2f}%")

    else:
        confidence = probability[0][0] * 100

        st.success("✅ Prediction:  Not Diabetic")

        st.write(f"Confidencce: {confidence:.2f}%")
