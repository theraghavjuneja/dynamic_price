import pandas as pd
import streamlit as st
import joblib

model = joblib.load("randomforest.pkl")

@st.cache_data
def load_data():
    data = pd.read_csv("indian-cities-dataset.csv")
    return data

city_data = load_data()

st.title("City Distance Calculator")

origin = st.selectbox("Origin", city_data["Origin"].unique())
valid_destinations = city_data[city_data["Origin"] == origin]["Destination"].unique()
destination = st.selectbox("Destination", valid_destinations)

distance = city_data[(city_data["Origin"] == origin) & (city_data["Destination"] == destination)]["Distance"].values

if len(distance) > 0:
    distance_km = distance[0]
    time_hours = distance_km / 60  # Assuming constant speed of 60 km/hr
    st.write(f"The distance between {origin} and {destination} is {distance_km} kilometers.")
    st.write(f"The time taken to travel is {time_hours:.2f} hours at a constant speed of 60 km/hr.")
else:
    st.write("Sorry, no data available for the selected cities.")
