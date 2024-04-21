import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import MinMaxScaler

model = joblib.load("randomforest.pkl")

@st.cache_data
def load_data():
    data = pd.read_csv("indian-cities-dataset.csv")
    return data

city_data = load_data()

origin = st.selectbox("Origin", city_data["Origin"].unique())
valid_destinations = city_data[city_data["Origin"] == origin]["Destination"].unique()
destination = st.selectbox("Destination", valid_destinations)
distance = city_data[(city_data["Origin"] == origin) & (city_data["Destination"] == destination)]["Distance"].values
time = distance / 60

st.write(time)
st.write(distance)

# Inputs integrated into main screen
number_of_riders = st.number_input("Number of Riders:", value=90)
number_of_drivers = st.number_input("Number of Drivers:", value=45)
number_of_past_rides = st.number_input("Number of Past Rides:", value=13)
average_ratings = st.number_input("Average Ratings:", value=4.47)
expected_ride_duration = st.number_input("Expected Ride Duration:", value=90)

# Min-max scaling
scaler = MinMaxScaler()
number_of_riders_scaled = scaler.fit_transform([[number_of_riders]])[0][0]
number_of_drivers_scaled = scaler.transform([[number_of_drivers]])[0][0]
number_of_past_rides_scaled = scaler.transform([[number_of_past_rides]])[0][0]
average_ratings_scaled = scaler.transform([[average_ratings]])[0][0]
expected_ride_duration_scaled = scaler.transform([[expected_ride_duration]])[0][0]
st.write(number_of_drivers_scaled)
time_of_booking = st.selectbox("Time of Booking:", ["Morning", "Afternoon", "Evening", "Night"])
if time_of_booking == "Morning":
    time_of_booking_morning = 1
    time_of_booking_evening = 0
    time_of_booking_night = 0
elif time_of_booking=='Afternoon':
    time_of_booking_morning=0
    time_of_booking_evening=0
    time_of_booking_night=0
elif time_of_booking=="Evening":
    time_of_booking_morning=0
    time_of_booking_evening=1
    time_of_booking_night=0
elif time_of_booking=="Night":
    time_of_booking_morning=0
    time_of_booking_evening=0
    time_of_booking_night=1

customer_loyalty_status = st.selectbox("Customer Loyalty Status:", ["Regular", "Silver", "Gold"])
if customer_loyalty_status == "Regular":
    customer_loyalty_status_regular = 1
    customer_loyalty_status_silver = 0
elif customer_loyalty_status == "Silver":
    customer_loyalty_status_regular = 0
    customer_loyalty_status_silver = 1
elif customer_loyalty_status == "Gold":
    customer_loyalty_status_regular = 0
    customer_loyalty_status_silver = 0

location_category = st.selectbox("Location Category:", ["Suburban", "Urban", "Rural"])
if location_category == "Suburban":
    location_category_suburban = 1
    location_category_urban = 0
elif location_category == "Urban":
    location_category_suburban = 0
    location_category_urban = 1
elif location_category == "Rural":
    location_category_suburban = 0
    location_category_urban = 0

vehicle_type_premium = st.selectbox("Vehicle Type (Premium):", [0, 1])

# Make prediction when the user clicks a button
if st.button("Predict"):
    input_data = [[number_of_riders_scaled, number_of_drivers_scaled, number_of_past_rides_scaled, average_ratings_scaled,
                   expected_ride_duration_scaled, time_of_booking_evening, time_of_booking_morning,
                   time_of_booking_night, customer_loyalty_status_regular, customer_loyalty_status_silver,
                   location_category_suburban, location_category_urban, time_of_booking_evening,
                   time_of_booking_morning, time_of_booking_night, vehicle_type_premium]]

    # Predict using the model
    prediction = model.predict(input_data)
    
    # Display prediction
    st.write(f"Prediction: {prediction}")
