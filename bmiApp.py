import streamlit as st
#bmi=weight/height2
st.title("BMI Calculation Master")
weight = st.number_input("Enter your weight (in kgs)")
status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

if(status == 'cms'): 
# take height input in centimeters 
  height = st.number_input('Centimeters') 
  try: bmi = weight / ((height/100)**2) 
  except: st.text("Enter some value of height") 
elif(status == 'meters'): 
# take height input in meters 
  height = st.number_input('Meters') 
  try: bmi = weight / (height ** 2) 
  except: st.text("Enter some value of height") 
else: # take height input in feet 
  height = st.number_input('Feet') 
# 1 meter = 3.28 
  try: bmi = weight / (((height/3.28))**2) 
  except: st.text("Enter some value of height") 

# check if the button is pressed or no
if(st.button('Calculate BMI')): 
  # print the BMI INDEX 
  st.text("Your BMI Index is {}.".format(bmi))
  
