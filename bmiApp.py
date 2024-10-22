import streamlit as st

st.title("BMI Calculation Master")
weight = st.number_input("Enter your weight (in kgs)")
status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))
