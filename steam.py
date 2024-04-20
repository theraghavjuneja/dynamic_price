import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    data = pd.read_csv("indian-cities-dataset.csv")
    return data
city_data = load_data()
st.title("City Distance Calculator")
st.sidebar.header("Select Cities")
origin = st.sidebar.selectbox("Origin", city_data["Origin"].unique())
valid_destinations = city_data[city_data["Origin"] == origin]["Destination"].unique()
destination = st.sidebar.selectbox("Destination", valid_destinations)
distance = city_data[(city_data["Origin"] == origin) & (city_data["Destination"] == destination)]["Distance"].values
if len(distance) > 0:
    st.write(f"The distance between {origin} and {destination} is {distance[0]} kilometers.")
else:
    st.write("Sorry, no data available for the selected cities.")
