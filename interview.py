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

hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Writing', 'Sports', 'Video Games', 'Others']) 
# print the selected hobby 
st.write("Your hobby is: ", hobby)

hobby = st.selectbox("Education: ", ['Secondary', 'Tertiery Bsc', 'Tertiery MSc', 'Others']) 

st.markdown("### Quick Qizz Session")
quest1 = st.selectbox("How many states in Nigeria? ", ['30', '25', '36', '46', 'Others']) 
quest2 = st.selectbox("How many planets in our solar system? ", ['5', '9', '7', '8', 'Others']) 
quest3 = st.number_input("What year did Nigeria gain independence?")
quest4 = st.text_input("What is  12 + 5 - 2 (3+5) ?", "0")

counter=0
if(st.button("Submit")): 
     if quest1 == "36":
          counter+=1
     elif quest2 == "8": 
          counter+=1
     elif quest3 == 1960: 
          counter+=1 
     elif quest4 == "1": 
          counter+=1        
     st.text("Thanks for participating. You got ", counter, " of 4 correctly.")


