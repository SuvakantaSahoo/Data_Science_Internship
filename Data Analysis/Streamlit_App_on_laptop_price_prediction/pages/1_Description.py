import streamlit as st
from matplotlib import image
import os
import pandas as pd
st.title(':blue[Laptop Price Predictor]')

st.markdown("""
    <style>
        body {
            background-image: url("https://cdn.wallpapersafari.com/65/31/UnM5q2.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)




#df = pd.read_csv(DATA_PATH)
#st.dataframe(df)

st.header(":orange[Introduction]")
st.write("""The task is to build a laptop price predictor that takes input of laptop features like RAM size, RAM type, HDD, OS, etc. and predicts the selling price of the laptop. This predictor should be based on data collected from various sources and should be accurate and reliable. The laptop price predictor should help users make informed decisions when buying or selling laptops and should provide valuable insights into the relationship between different laptop features and their selling price.""")
st.header(':red[Goal]')
st.write("""The goal of this project is to help Tesla Laptop gain a competitive edge in the Indian laptop market by building a streamlit interface that allows users to input laptop features and get a predicted price. The project also aims to analyze the data collected from various competitors to provide insights into the relationship between different laptop features and their selling price. Based on these insights, recommendations will be given to Tesla Laptop to make informed pricing decisions that will enable them to compete with established brands and increase their market share in India""")

st.header("Dataset")
url = 'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
st.markdown("""This is real world data. It was scrapped from Flipkart on 21-12-2022 at 11:50 AM.
Here is the link :
{}
""".format(url))

