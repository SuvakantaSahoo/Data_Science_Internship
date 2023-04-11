import streamlit as st
from matplotlib import image
import os
import io
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.markdown("""
    <style>
        body {
            background-image: url("https://unbox.ph/wp-content/uploads/2021/10/Photo-Release-3_HUAWEI-Brings-Laptop-MateBook-14s-and-nova-9-in-PH-scaled.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.2);
        }
    </style>
""", unsafe_allow_html=True)


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "laptop_data.csv")
st.title(":green[Laptop Data Info]")



st.header(':red[DataFrame]')

df = pd.read_csv(DATA_PATH)
st.dataframe(df)


st.header(":blue[Details of the Dataset]")

data_info = st.radio('Click to view the Details of the Dataset:',
                      ('Head', 'Tail','Sample', 'Columns', 'Shape', 'Info', 'Descriptive Statistics'),
                      horizontal=True)

if data_info == 'Shape':
    st.write(f"Number of Rows:  {df.shape[0]}")
    st.write(f"Number of Columns:  {df.shape[1]}")
elif data_info == 'Head':
    st.write(df.head())
elif data_info == 'Tail':
    st.write(df.tail())
elif data_info == 'Sample':
    st.write(df.sample(10))  
elif data_info == 'Columns':
    for column in list(df.columns):
        st.write(column)
elif data_info == 'Info':
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
else:
    st.write(df.describe())
