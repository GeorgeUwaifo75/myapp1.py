import streamlit as st

import time

#st.set_page_config()

ph = st.empty()
N = 0.5*60
for secs in range(N,0,-1):
    mm, ss = secs//60, secs%60
    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
    time.sleep(1)
st.set_page_config()

st.title("Interview Session")
st.text("This is a set of questions for this interview session")
fname = st.text_input("What is your first name?", "Enter name")

lname = st.text_input("What is your last name?", "Enter name")

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
q1 = int(quest1)
quest2 = st.selectbox("How many planets in our solar system? ", ['5', '9', '7', '8', 'Others']) 
q2 = int(quest2)
quest3 = st.text_input("What year did Nigeria gain independence?","")

try: q3 = int(quest3)
except:  st.text("Enter a valid year!!!")     

quest4 = st.text_input("What is  12 + 5 - 2 (3+5) ?","")
try: q4 = int(quest4)
except:  st.text("Enter a valid number!!!") 
counter=0
if(st.button("Submit")): 
     if q1 == 36:
          counter+=1
     if q2 == 8: 
          counter+=1
     if q3 == 1960: 
          counter+=1 
     if q4 == 1: 
          counter+=1 
     perct = ((counter/4) * 100)     
     st.write("Thanks ",lname," ",fname, " for participating. You got ", counter, " of 4 correctly, which is ",perct, "%")


