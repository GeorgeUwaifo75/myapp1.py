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

hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports']) 
# print the selected hobby 
st.write("Your hobby is: ", hobby)

# multi select box # first argument takes the box title # second argument takes the options to show 
hobbies = st.multiselect("Hobbies: ", ['Dancing', 'Reading', 'Sports']) 
# write the selected options 
st.write("You selected", len(hobbies), 'hobbies')

# Create a simple button that does nothing 
st.button("Click me for now") 
# Create a button, that when clicked, shows a text 
if(st.button("About")): 
   st.text("Welcome To GiTeksol Hub!!!")
   
name = st.text_input("Enter Your name", "Type Here ...")
if(st.button('Submit')): 
   result = name.title() 
   st.success(result)

