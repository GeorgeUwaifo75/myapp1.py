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

#filter rows on the basis of date 
newdf = (df['date'] > begin_val) & (df['date'] <= end_val)  & (df['open'] >= price_val)

#locate rows and access them using .loc() function 
newdf = df.loc[newdf] 

#print dataframe 
st.write(newdf) 


df2 = newdf.sort_values('date', ascending=True)


#plt.plot(df2['date'], df2['high'])
#st.line_chart(df2['date'], df2['high'])
#plt.xticks(rotation='vertical')

x= df2['date']
y = df2['high']


the_chart = pd.DataFrame([x,y], columns=["a", "b"])
#chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart( the_chart )

z = np.percentile(df2['high'], 25)

st.write(z) 
