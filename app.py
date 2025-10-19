import streamlit as st
import pandas as pd
import pickle

# Load the trained regression model
with open("model-reg-ุ67130701918.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Sales Prediction App")

st.write("Enter ad spending for each platform:")

youtube = st.number_input("YouTube", min_value=0, max_value=1000, value=50)
tiktok = st.number_input("TikTok", min_value=0, max_value=1000, value=50)
instagram = st.number_input("Instagram", min_value=0, max_value=1000, value=50)

# Prepare input data
input_data = pd.DataFrame({
    "youtube": [youtube],
    "tiktok": [tiktok],
    "instagram": [instagram]
})

# Make prediction
predicted_sales = model.predict(input_data)[0]

st.write(f"💡 Predicted Sales: {predicted_sales:.2f}")
