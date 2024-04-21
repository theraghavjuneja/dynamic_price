import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import MinMaxScaler

model = joblib.load("regressor.pkl")
def return_actual_pred(prediction,distance):
    if 10*distance<prediction:
        return prediction
    else:
        return 10*distance
    
@st.cache_data
def load_data():
    data = pd.read_csv("indian-cities-dataset.csv")
    return data

city_data = load_data()

origin = st.selectbox("Origin", city_data["Origin"].unique())
valid_destinations = city_data[city_data["Origin"] == origin]["Destination"].unique()
destination = st.selectbox("Destination", valid_destinations)
distance = city_data[(city_data["Origin"] == origin) & (city_data["Destination"] == destination)]["Distance"].values
time_in_minutes = (distance / 55) * 60
st.write(f"Estimated Time: {time_in_minutes} minutes")

# Inputs integrated into main screen
number_of_riders = st.number_input("Number of Riders:", value=90)
number_of_drivers = st.number_input("Number of Drivers:", value=45)
number_of_past_rides = st.number_input("Number of Past Rides:", value=13)
average_ratings = st.number_input("Average Ratings:", value=4.47)
estimated_ride_duration = st.number_input("Expected Ride Duration:", value=float(time_in_minutes))
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

if st.button("Predict"):
    input_data = [[number_of_riders, number_of_drivers, number_of_past_rides, average_ratings,
                   estimated_ride_duration, time_of_booking_evening, time_of_booking_morning,
                   time_of_booking_night, customer_loyalty_status_regular, customer_loyalty_status_silver,
                   location_category_suburban, location_category_urban, time_of_booking_evening,
                   time_of_booking_morning, time_of_booking_night, vehicle_type_premium]]
    per_km=10
    prediction = model.predict(input_data)
    prediction=return_actual_pred(prediction,distance)
    st.write(prediction)
    rt=number_of_riders/number_of_drivers
    adjusted_prediction = prediction * rt
    st.write(f"Adjusted Prediction: {adjusted_prediction}")
