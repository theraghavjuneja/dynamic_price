import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

st.title("Distance and Time Calculator")

# Sidebar inputs for source and destination
source = st.text_input("Enter source location:", "")
destination = st.text_input("Enter destination location:", "")

# Average speed in km/h
average_speed = 40  # Assume average speed is 40 km/h

# Function to get coordinates from location name
def get_coordinates(location):
    geolocator = Nominatim(user_agent="distance_calculator")
    try:
        location = geolocator.geocode(location)
        return (location.latitude, location.longitude)
    except:
        st.error("Location not found.")
        return None

# Calculate distance and time if both source and destination are provided
if source and destination:
    source_coordinates = get_coordinates(source)
    destination_coordinates = get_coordinates(destination)
    
    if source_coordinates and destination_coordinates:
        distance = geodesic(source_coordinates, destination_coordinates).kilometers
        time_hours = distance / average_speed
        time_minutes = time_hours * 60
        st.success(f"Distance between {source} and {destination}: {distance:.2f} kilometers")
        st.success(f"Estimated time to travel: {time_hours:.2f} hours ({time_minutes:.2f} minutes)")
