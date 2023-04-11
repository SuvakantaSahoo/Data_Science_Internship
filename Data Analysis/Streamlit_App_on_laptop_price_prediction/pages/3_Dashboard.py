import streamlit as st
from matplotlib import image
import os
import io
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import statsmodels.api as sm

st.markdown("""
    <style>
        body {
            background-image: url("https://wallpaperaccess.com/full/1924555.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
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
st.title(":red[Laptop Dashboard]")
df = pd.read_csv(DATA_PATH)
col1=st.columns(1)
fig_1 = px.histogram(df,x=df['MRP'],color='RAM',title='Laptop Price Distribution')
st.plotly_chart(fig_1, use_container_width=True)

fig = px.sunburst(df, path=['Brand', 'Rating'], title='Brand and Rating',values='MRP')
st.plotly_chart(fig, use_container_width=True)




fig_3 = px.bar(df, x='Brand', y='MRP', color='Brand', title='Laptop price with respect to their Brands')
st.plotly_chart(fig_3, use_container_width=True)


fig_4 = px.bar(df,x= df['CPU'],y = df['MRP'],color='CPU',title = 'Laptop Price with respect to Processor')
st.plotly_chart(fig_4,use_container_width=True)

fig = px.scatter(df, x="RAM", y="MRP", color='RAM',trendline="ols", title="RAM vs. MRP")
st.plotly_chart(fig, use_container_width=True)

fig_6 = px.scatter(df,x = df['SSD_GB'],y = df['MRP'],color='Brand',title = 'Laptp Price with respect to Storage SSD')
st.plotly_chart(fig_6,use_container_width=True)
fig_7 = px.scatter(df,x = df['HDD_GB'],y = df['MRP'],color='Brand',title = 'Laptop Price with respect to Storage HDD')
st.plotly_chart(fig_7,use_container_width=True)

fig = px.bar(df, x='OS', y='MRP',color='CPU', title='Price variation with OS')
st.plotly_chart(fig, use_container_width=True)

grouped_df = df.groupby(['OS', 'RAM']).mean().reset_index()

fig = px.bar(grouped_df, x='RAM', y='MRP', color='OS', barmode='group')
fig.update_layout(title='Price variation with RAM and OS', xaxis_title='RAM', yaxis_title='Price (INR)')
st.plotly_chart(fig, use_container_width=True)
