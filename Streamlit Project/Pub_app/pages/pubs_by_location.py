import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static


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
st.markdown("<h2 style='text-align: center; color: #5243AA;'>Pub Locations</h2>", unsafe_allow_html=True)

# Make a new dataframe
df_pubs=pub_data[['name','postcode','local_authority','latitude','longitude']]

# Allow user to choose between searching by postal code or local authority
search_type = st.radio("Search by:", ('Postal Code', 'Local Authority'))

# Create a list of unique postal codes or local authorities to display in the dropdown menu
if search_type == 'Postal Code':
    search_list = sorted(df_pubs['postcode'].unique())
else:
    search_list = sorted(df_pubs['local_authority'].unique())

# Allow user to select a postal code or local authority from the dropdown menu
search_value = st.selectbox(f"Select a {search_type}:", search_list)

# Filter the dataset based on the selected postal code or local authority
if search_type == 'Postal Code':
    desired_pubs  = df_pubs[df_pubs['postcode'] == search_value]
else:
    desired_pubs  = df_pubs[df_pubs['local_authority'] == search_value]

# Display the filtered dataset
st.write(f"Displaying {len(desired_pubs)} pubs in {search_value}:")
st.dataframe(desired_pubs)

# Create a map centered on the desired area
map_center = [desired_pubs['latitude'].mean(), desired_pubs['longitude'].mean()]

pubs_map = folium.Map(location=map_center, zoom_start=13)

# Add markers for each pub to the map
for index, row in desired_pubs.iterrows():
    pub_location = [row['latitude'], row['longitude']]
    pub_name = row['name']
    pub_marker = folium.Marker(location=pub_location, popup=pub_name)
    pub_marker.add_to(pubs_map)

# Display the map
folium_static(pubs_map)

