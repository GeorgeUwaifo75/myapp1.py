import streamlit as st
import time

def count_down(ts):
    with st.empty():
        while ts:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"{time_now}")
            time.sleep(1)
            ts -= 1
        st.write("Time Up!")

def form_body():
    st.title("Pomodoro")
    fname = st.text_input('Enter first name ', '')
    lname = st.text_input('Enter last name ', '')
    
def main():
   # st.title("Pomodoro")
   # time_minutes = st.number_input('Enter the time in minutes ', min_value=1, value=25)
   form_body()
   time_in_seconds = time_minutes * 60
   count_down(int(120))
   # if st.button("START"):
   #      count_down(int(time_in_seconds))
if __name__ == '__main__':
    main()
