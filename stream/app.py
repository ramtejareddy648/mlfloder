import streamlit as st 
import pandas as pd
import numpy as np


st.title("this is title")
st.header("this is header")
st.subheader("this sub header")

st.write("this is write tag")
df=pd.DataFrame(
    {
    "A":[1,2,3,4],
    "B":[6,7,89,9]
    }
)
st.write(df)


chart=pd.DataFrame(
    np.random.randn(20,3), columns=["A","B","C"]
)
st.write(chart)
st.line_chart(chart)


df1=pd.DataFrame(
    np.random.randint(1,20,size=(4,3)),columns=["A","B","C"]
)

st.write(df1)


name=st.text_input("enter your name:")
if name:
    st.write(f"your name is {name}")

rating=st.slider("enter your rating",0,5,0)
st.write(f"your rating is {rating}")


options=["python","c++","java","dbms","ds","c"]
choice=st.selectbox("choose your option",options=options)
st.write(choice)



data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
df.to_csv("data.csv")
st.write(df)


upload=st.file_uploader("upload your file",type="csv")

if upload is not None:
    df=pd.read_csv(upload)
    st.write(df)
data =({
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
)

st.table(data)

st.metric(label="wind speed",value="70ms",delta="-5.7")
st.markdown("this is so jay:joy:")

