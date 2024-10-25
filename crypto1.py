import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn import linear_model

st.header("Crypto Analytics Buddy")
n=1
try:
    n = int(st.text_input("Enter 1-Doge, 2-Shib, 3-LTC,4-SOL, 5-XMR : "))
except:
    st.write("Enter correct value.")

if n==1:
    dataFile = 'DOGE.csv'
elif n==2:   
    dataFile = 'DOGE.csv'
elif n==3:   
    dataFile = 'DOGE.csv'
elif n==4:   
    dataFile = 'DOGE.csv'
elif n==5:   
    dataFile = 'DOGE.csv'    

df = pd.read_csv(dataFile)
# Remove missing values
df.dropna(inplace=True)

st.write(df.info())
#print(df.describe())
#print(df.head())

#convert date column into date format 
df['date'] = pd.to_datetime(df['date']) 

begin_val = input("Begin date : ")
if begin_val == "":
    begin_val = '2010-07-17'
end_val = input("End date : ")
if end_val == "":
    end_val = '2024-10-24'

price_val =0
try:
   price_val = float(input("Start price : "))
except:
    price_val = 0.001
