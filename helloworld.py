import streamlit as st
st.title("Hello world my friend")

from PIL import Image 
img = Image.open("streamlit.png") 
st.image(img, width=200)
