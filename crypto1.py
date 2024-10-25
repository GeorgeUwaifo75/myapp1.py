import streamlit as st


st.header("My crypto hub")
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn import linear_model

dataFile = 'DOGE.csv'
df = pd.read_csv(dataFile)

# Remove missing values
df.dropna(inplace=True)

print(df.info())
print(df.describe())
print(df.head(5))
