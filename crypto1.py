import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn import linear_model

st.header("Crypto Analytics Buddy")
n = int(input("Enter 1-Doge, 2-Shib, 3-LTC,4-SOL, 5-XMR : "))

# dataFile = 'DOGE.csv'
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
