import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn import linear_model

st.header("My Predict Buddy*+")

try:
    n = int(st.text_input("Enter 1-Doge, 2-Shib, 3-LTC, 4-SOL, 5-XMR: "))
except:
    st.write("Enter correct value.")

if n==1:
        dataFile = 'Binance_DOGEUSDT_1h.csv'
elif n==2:   
        dataFile = 'Binance_SHIBUSDT_1h.csv'
elif n==3:   
        dataFile = 'Binance_LTCUSDT_1h.csv'
elif n==4:   
        dataFile = 'Binance_SOLUSDT_1h.csv'
elif n==5:   
        dataFile = 'Binance_XMRUSDT_1h.csv'    

df = pd.read_csv(dataFile)

# Remove missing values
df.dropna(inplace=True)

st.write(df.head(5))
X = df[['Open', 'Volume USDT']]
y = df['High']

regr = linear_model.LinearRegression()
regr.fit(X, y)
#print(regr.coef_) 

if st.button("Start"):
    st.write(df.describe())
   
    try:
        op_val = float(st.number_input("Open Value : "))
    except:
        op_val = float(0.059)
  
    try:
        vol_val = st.number_input("Volume Value : ")
    except:
        vol_val = int(1000)  
      
    if op_val>0 & vol_val>0:
            if st.button("Predict Value"):
                predictedHigh = regr.predict([[v1, v2]])
                st.write("The highest pedicted value:",predictedHigh) 
    #doPhase2(op_val,vol_val)

#def doPhase2(v1,v2):
#    predictedHigh = regr.predict([[v1, v2]])
#    st.write("The highest pedicted value:",predictedHigh) 
