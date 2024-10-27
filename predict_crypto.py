import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn import linear_model


st.header("My Predict Buddy")

n = int(input("Enter 1-Doge, 2-Shib, 3-LTC,4-SOL, 5-XMR : "))

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

print(df.info())
#print(df.describe())
print(df.head(5))

#----Doge
#Get the relationship between the x & y(High) variables
#x= df['Open'] #R: 0.999738450769844
#y= df['High'] #R:  0.9996819053118083
#y= df['Low'] #R:  0.9992441066334198
#y= df['Close'] #R:  0.999611820080495
#y= df['Volume DOGE'] #R:  0.15564750585272383
#y= df['Volume USDT'] #R:  0.46920371020546875
#y= df['tradecount'] #R:  0.500517120518652

X = df[['Open', 'Volume USDT']]
y = df['High']
#y = df['Low']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#print(regr.coef_) 

print(df.describe())

op_val = float(input("Open Value : "))
vol_val = int(input("Volume Value : "))

predictedHigh = regr.predict([[op_val, vol_val]])

print("The highest pedicted value:",predictedHigh) 
