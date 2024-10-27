import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn import linear_model

def doPhase2(v1,v2):
    predictedHigh = regr.predict([[v1, v2]])
    st.write("The highest pedicted value:",predictedHigh) 

def doPhase1():
    df = pd.read_csv(dataFile)

    # Remove missing values
    df.dropna(inplace=True)

    #print(df.info())
    #print(df.describe())
    st.write(df.head(5))
    X = df[['Open', 'Volume USDT']]
    y = df['High']
    #y = df['Low']

    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    #print(regr.coef_) 

    st.write(df.describe())

    #try:
     #  op_val = float(st.number_input("Open Value : "))
    #except:
     #   op_val = 0.059

    #try:
     #  vol_val = int(st.number_input("Volume Value : "))
    #except:
     #  vol_val = 1000  
    
    # vol_val = int(st.text_input("Volume Value : "))
    
    #if vol_val > 1000:
    #if st.button("Predict Value"):
     #   doPhase2(op_val,vol_val)


#def doMain():
st.header("My Predict Buddy")
n=0
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

if st.button("Start"):
    doPhase1()
    try:
       op_val = float(st.number_input("Open Value : "))
    except:
        op_val = 0.059
    try:
       vol_val = int(st.number_input("Volume Value : "))
    except:
       vol_val = 1000  
    
    if st.button("Predict Value"):
        pass
       # doPhase2(op_val,vol_val)
#doMain()
#----Doge
#Get the relationship between the x & y(High) variables
#x= df['Open'] #R: 0.999738450769844
#y= df['High'] #R:  0.9996819053118083
#y= df['Low'] #R:  0.9992441066334198
#y= df['Close'] #R:  0.999611820080495
#y= df['Volume DOGE'] #R:  0.15564750585272383
#y= df['Volume USDT'] #R:  0.46920371020546875
#y= df['tradecount'] #R:  0.500517120518652



