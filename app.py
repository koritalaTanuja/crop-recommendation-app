import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("crop_model.pkl", "rb"))

st.title("🌾 Crop Recommendation System")

st.write("Enter soil and weather values to predict the best crop.")

N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorus (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
ph = st.number_input("pH Value", min_value=0.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

if st.button("Predict Crop"):
    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(data)
    st.success(f"Recommended Crop: {prediction[0]}")