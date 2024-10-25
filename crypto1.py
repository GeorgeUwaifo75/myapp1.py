import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn import linear_model

st.header("Crypto Analytics Buddy")
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
    dataFile = 'Binance_XMRUSDT_1h.csv'    
