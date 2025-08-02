import streamlit as st
import pickle 
import numpy as np
import os

model_path = 'winequality.pkl'

if not os.path.exists(model_path):
    st.error(f"Model file not found at: {model_path}")
else:
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
    except Exception as e:
        st.error(f"Failed to load model: {e}")

with open('wine_quality_pred.pkl', 'rb') as f:
    model = pickle.load(f)

st.header("Wine Quality Prediction")
st.subheader("Adjust the sliders to predict the quality of a wine quality")

votaltile_acidity = st.slider("Volatile Acidity",0.0,2.0)
citric_acid = st.slider("Citric Acid",0.0,1.0)
sulphates = st.slider("Sulphates",0.0,2.0)
alcohol = st.slider("Alcohol",0.0,15.0)

input_data = [votaltile_acidity,citric_acid,sulphates,alcohol]

if st.button("Predict"):
    result = model.predict([input_data])
    if result[0] == 1:
        st.success("Wine quality is Good")
    else:
        st.error("Wine quality is Bad")

