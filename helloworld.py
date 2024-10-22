import streamlit as st
st.title("Hello world my friend")

st.text("Hello GeeksForGeeks!!!")

st.success("Success") 
st.info("Information") 
st.warning("Warning") 
st.error("Error") 
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

st.write("Text with write") 
st.write(range(10))
