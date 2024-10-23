import streamlit as st

st.title("Interview Session")
st.text("This is a set of questions for this interview session")
fname = st.text_input("What is your first name?", "Enter name")
if fname:
     st.write("Your first name is ", fname)
     lname = st.text_input("What is your last name?", "Enter name")
if lname:
     st.write("Your last name is ", lname)
     status = st.radio("Select Gender: ", ('Male', 'Female')) 

# conditional statement to print 
if (status == 'Male'): 
     st.success("Male") 
else: 
     st.success("Female")
