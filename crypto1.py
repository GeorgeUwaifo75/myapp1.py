import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn import linear_model

st.header("Crypto Analytics Buddy")
n=1
try:
    n = int(st.text_input("Enter 1-Doge, 2-Shib, 3-LTC, 4-SOL, 5-XMR, 6-BTC, 7-ETH : "))
except:
    st.write("Enter correct value.")

if n==1:
    dataFile = 'DOGE.csv'
elif n==2:   
    dataFile = 'SHIB.csv'
elif n==3:   
    dataFile = 'LTC.csv'
elif n==4:   
    dataFile = 'SOL.csv'
elif n==5:   
    dataFile = 'XMR.csv'    
elif n==6:   
    dataFile = 'BTC.csv'
elif n==7:   
    dataFile = 'ETH.csv'    

df = pd.read_csv(dataFile)
# Remove missing values
df.dropna(inplace=True)

st.write(df.info())
#print(df.describe())
#print(df.head())

#convert date column into date format 
df['date'] = pd.to_datetime(df['date']) 

begin_val = st.text_input("Begin date : ",'2010-07-17')
if begin_val == "":
    begin_val = '2010-07-17'
end_val = st.text_input("End date : ",'2024-10-24')
if end_val == "":
    end_val = '2024-10-24'

price_val =0
try:
   price_val = float(st.number_input("Start price : "))
except:
    price_val = 0.001

def genVisual():
    #filter rows on the basis of date 
    newdf = (df['date'] > begin_val) & (df['date'] <= end_val)  & (df['open'] >= price_val)

    #locate rows and access them using .loc() function 
    newdf = df.loc[newdf] 

    #print dataframe 
    st.write(newdf) 

    df2 = newdf.sort_values('date', ascending=True)

    column = st.selectbox('Select a column', df2.columns)
    title = st.text_input('Title', 'Line Plot')
    x_label = st.text_input('X-axis Label', 'X-axis')
    y_label = st.text_input('Y-axis Label', 'Y-axis')
    color = st.color_picker('Line Color', '#1f77b4')

    fig, ax = plt.subplots()
    ax.plot(df2['date'], df2['high'], color=color)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Rotate X-axis labels
    plt.xticks(rotation=45)

    st.pyplot(fig)


    z = np.percentile(df2['high'], 25)

    st.write("25% or less registers the high of ",z) 

if st.button("Generate Visual"):
     genVisual()
