import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk


car=pd.read_csv('cleaned.csv')

model=pk.load(open('linear.pkl','rb'))
##st.header('car price prediction')
st.markdown("""<h1 style='text-align:center;'>car price prediction</h1>""",unsafe_allow_html=True)
company=st.selectbox('enter car brand',car['company'].unique(),placeholder='car barand')
name=st.selectbox('enter car name',car['name'].unique(),placeholder='car name')
year=st.text_input('enter year',placeholder='year')
kms=st.text_input('enter kms',placeholder='kms')
fuel=st.selectbox('enter fuel type',car['fuel_type'].unique(),placeholder='fuel')
if st.button('prediction'):
   pred=model.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array([name,company,year,kms,fuel]).reshape(1,5)))
   st.write(pred)

