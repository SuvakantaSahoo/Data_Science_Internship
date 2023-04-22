import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Load the pub dataset
pub_data = pd.read_csv('open_pubs.csv', header=None)
pub_data.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

# Replace \N values with NaN
pub_data = pub_data.replace('\\N', np.nan)

# Drop rows with NaN values
pub_data = pub_data.dropna()

pub_data['longitude'] = pd.to_numeric(pub_data['longitude'], errors='coerce')
pub_data['latitude'] = pd.to_numeric(pub_data['latitude'], errors='coerce')

# Set the page layout to centered
st.set_page_config(layout="centered")

# Add some styling to the title and subtitle
st.markdown("<h1 style='text-align: center; color: #EB6864; font-weight: bold;'>🍺 Open Pubs Application 🍻</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #5243AA;'>Find the Nearest Pub</h2>", unsafe_allow_html=True)

# Make a new dataframe
df_pubs=pub_data[['name','postcode','local_authority','latitude','longitude']]

# Allow user to enter their latitude and longitude
lat = st.number_input("Enter your latitude:", value=51.73)
lon = st.number_input("Enter your longitude:", value=-4.72)

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

# Calculate the distance between the user's location and each pub in the dataset
df_pubs['distance'] = df_pubs.apply(lambda row: euclidean_distance(row['latitude'], row['longitude'], lat, lon), axis=1)

# Sort the dataset by distance and display the nearest 5 pubs
desired_pubs = df_pubs.sort_values(by='distance').head(5)
st.write(f"Displaying the 5 nearest pubs to your location (lat: {lat}, lon: {lon}):")
st.dataframe(desired_pubs)

pubs_map = folium.Map(location=(lat,lon), zoom_start=13)

# Add markers for each pub to the map
for index, row in desired_pubs.iterrows():
    pub_location = [row['latitude'], row['longitude']]
    pub_name = row['name']
    pub_marker = folium.Marker(location=pub_location, popup=pub_name)
    pub_marker.add_to(pubs_map)

# Display the map
st.write("Map of the nearest pubs:")
folium_static(pubs_map)

