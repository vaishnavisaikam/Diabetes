import streamlit as st

from predictor import predict_diabetes

from report import health_report

from database import save_patient


st.set_page_config(page_title="Diabetes Risk Assessment Agent", layout="wide")

st.title("🩺 Diabetes Risk Assessment Agent")

st.write("Enter Patient Details")

name = st.text_input("Patient Name")

preg = st.number_input("Pregnancies",0,20)

glu = st.number_input("Glucose",0.0)

bp = st.number_input("Blood Pressure",0.0)

skin = st.number_input("Skin Thickness",0.0)

insulin = st.number_input("Insulin",0.0)

bmi = st.number_input("BMI",0.0)

ped = st.number_input("Diabetes Pedigree Function",0.0)

age = st.number_input("Age",1,120)


if st.button("Predict"):

    patient = [

        preg,

        glu,

        bp,

        skin,

        insulin,

        bmi,

        ped,

        age

    ]

    prediction, probability = predict_diabetes(patient)

    risk, recommendation = health_report(probability)

    if prediction == 1:

        result = "Diabetic"

    else:

        result = "Non-Diabetic"

    st.subheader("Prediction")

    st.success(result)

    st.metric("Probability", f"{probability*100:.2f}%")

    st.subheader("Risk Level")

    st.info(risk)

    st.subheader("Recommendations")

    st.write(recommendation)

    save_patient(

        (

            name,

            preg,

            glu,

            bp,

            skin,

            insulin,

            bmi,

            ped,

            age,

            result,

            probability

        )

    )

    st.success("Patient record saved successfully.")