import streamlit as st
st.title("Hello world my friend")

st.checkbox("Show/Hide")
if st.checkbox("Show/Hide"): 
   st.text("Showing the widget")

