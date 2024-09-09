
#import libraries
import os
import streamlit as st
import numpy as np
import pickle 


# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Construct the full path to the model file
model_path = os.path.join(current_dir, 'crop_model.pkl')

# Load the model
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Set a custom page configuration
st.set_page_config(page_title="Crop Prediction App ", page_icon="🌱", layout="centered", initial_sidebar_state="expanded")

# Sidebar information
st.sidebar.title("Crop Prediction Info")
st.sidebar.info("""
This app predicts the most suitable crop based on the provided values for Nitrogen, Phosphorus, Potassium, and pH levels.
                
Made by Zeeshan Ahmad!
""")

# Title 
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

# Prediction button
if st.button('Predict Crop'):
    prediction = model.predict(input_data)
    st.markdown(f"<h2 style='text-align: center; color: darkbrown;'>🌱 The predicted crop is: {prediction[0].upper()}</h3>", unsafe_allow_html=True)

