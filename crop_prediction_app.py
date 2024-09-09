import streamlit as st
import numpy as np
import pickle 
from PIL import Image



# Assuming you saved it using pickle
with open('.\model\crop_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set a custom page configuration
st.set_page_config(page_title="Crop Prediction App ", page_icon="🌱", layout="centered", initial_sidebar_state="expanded")

# Sidebar information
st.sidebar.title("Crop Prediction Info")
st.sidebar.info("""
This app predicts the most suitable crop based on the provided values for Nitrogen, Phosphorus, Potassium, and pH levels.
                
Made by Zeeshan Ahmad!
""")

# Title with custom styling
st.markdown("<h1 style='text-align: center; color: green;'> Crop Prediction App 🌾</h1>", unsafe_allow_html=True)


# Get user input
def get_user_input():
    n = st.number_input("Nitrogen ", value=0)
    p = st.number_input("Phosphorus ", value=0)
    k = st.number_input("Potassium", value=0)
    ph = st.number_input("ph", value=0)
    return np.array([[n, p, k, ph]])

# Get prediction
input_data = get_user_input()
# Prediction button with custom color
if st.button('Predict Crop'):
    prediction = model.predict(input_data)
    st.markdown(f"<h2 style='text-align: center; color: darkbrown;'>🌱 The predicted crop is: {prediction[0].upper()}</h3>", unsafe_allow_html=True)

