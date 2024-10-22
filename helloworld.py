import streamlit as st
st.title("Hello world my friend")

if st.checkbox("Show/Hide"): 
   st.text("Showing the widget")

status = st.radio("Select Gender: ", ('Male', 'Female')) 
# conditional statement to print # Male if male is selected else print female # show the result using the success function 
if (status == 'Male'): 
   st.success("Male") 
else: 
   st.success("Female")

