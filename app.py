import streamlit as st
import pandas as pd
import numpy as np

# title
st.title("Streamlit Application.")
# text
st.write("This is a streamlit-text.")
# create df
df = pd.DataFrame({
    'col1':[1,2,3,4,5],
    'col2':[10,20,30,40,50]
})
st.write("Display DataFrame.")
st.write(df)
# linechart
chart = pd.DataFrame(
    np.random.randn(20, 5),columns=['a','b','c','d','e']
)
st.line_chart(chart)
# Widgets
# text i/p
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}")

# slider
age = st.slider("Select your age",0,100,18)
st.write(f"Age Entered is: {age}")

options = ['None','JS','C++','C', "python"]
# dropbox
lang = st.selectbox("Select your favorite programming language",options)

st.write(f"favorite programming language: {lang}")

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
df2 = pd.DataFrame(data)
st.write(df2)

# upload file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt",'bin','png','jpg','jpeg'])
st.write(uploaded_file)

# display image
uploaded_image = st.file_uploader("Choose an image", type=["png", "jpg"])
if uploaded_image is not None:
    st.image(uploaded_image, caption='Uploaded Image', width=200)
