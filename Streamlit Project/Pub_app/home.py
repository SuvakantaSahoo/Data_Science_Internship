import streamlit as st
import pandas as pd
import numpy as np

# Load the pub dataset
pub_data = pd.read_csv('open_pubs.csv', header=None)
pub_data.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

# Replace \N values with NaN
pub_data = pub_data.replace('\\N', np.nan)

# Drop rows with NaN values
pub_data = pub_data.dropna()

# Set the page layout to centered
st.set_page_config(layout="centered")

# Add some styling to the title and subtitle
st.markdown("<h1 style='text-align: center; color: #EB6864; font-weight: bold;'>🍺 Open Pubs Application 🍻</h1>", unsafe_allow_html=True)

# Add an image of a pub
st.image('pubimage.png', use_column_width=True)

# Display some basic information about the dataset
st.write(f"The dataset contains **{len(pub_data)}** pub locations.")
st.write(f"The dataset covers **{len(pub_data['local_authority'].unique())}** local authorities.")
st.markdown("<h2 style='text-align: center; color: #7F45FA;'>Pub Data! </h2>", unsafe_allow_html=True)
st.markdown("<style>div.stDataFrame div[data-testid='stHorizontalBlock'] div[data-testid='stDataFrameContainer'] {margin: 0 auto;}</style>", unsafe_allow_html=True)
st.write(pub_data)

#  Information about dataset
st.write("**Information about dataset**")
st.write('Total Pub names :',pub_data['name'].nunique())
st.write('Pub address :',pub_data['address'].nunique())
st.write('Postcode :',pub_data['postcode'].nunique())
st.write('Local_authority :',pub_data['local_authority'].nunique())


