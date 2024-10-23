import streamlit as st

st.title("Interview Session")
st.text("This is a set of questions for this interview session")
fname = st.text_input("What is your first name?", "Enter your first name...")
if fname !="":
  st.text("Your first name is ", fname)
