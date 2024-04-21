import pandas as pd
import streamlit as st
import joblib
model = joblib.load("randomforest.pkl")

number_of_riders = st.sidebar.number_input("Number of Riders:", value=0.875)
number_of_drivers = st.sidebar.number_input("Number of Drivers:", value=0.556)
number_of_past_rides = st.sidebar.number_input("Number of Past Rides:", value=0.13)
average_ratings = st.sidebar.number_input("Average Ratings:", value=0.646)
expected_ride_duration = st.sidebar.number_input("Expected Ride Duration:", value=0.471)
time_of_booking = st.sidebar.selectbox("Time of Booking:", ["Morning", "Afternoon", "Evening", "Night"])
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
customer_loyalty_status = st.sidebar.selectbox("Customer Loyalty Status:", ["Regular", "Silver", "Gold"])
if customer_loyalty_status == "Regular":
    customer_loyalty_status_regular = 1
    customer_loyalty_status_silver = 0
elif customer_loyalty_status == "Silver":
    customer_loyalty_status_regular = 0
    customer_loyalty_status_silver = 1
elif customer_loyalty_status == "Gold":
    customer_loyalty_status_regular = 0
    customer_loyalty_status_silver = 0
location_category = st.sidebar.selectbox("Location Category:", ["Suburban", "Urban", "Rural"])
if location_category == "Suburban":
    location_category_suburban = 1
    location_category_urban = 0
elif location_category == "Urban":
    location_category_suburban = 0
    location_category_urban = 1
elif location_category == "Rural":
    location_category_suburban = 0
    location_category_urban = 0
vehicle_type_premium = st.sidebar.selectbox("Vehicle Type (Premium):", [0, 1])

# Make prediction when the user clicks a button
if st.sidebar.button("Predict"):
    # Prepare input data
    input_data = [[number_of_riders, number_of_drivers, number_of_past_rides, average_ratings,
                   expected_ride_duration, time_of_booking_evening, time_of_booking_morning,
                   time_of_booking_night, customer_loyalty_status_regular, customer_loyalty_status_silver,
                   location_category_suburban, location_category_urban, time_of_booking_evening,
                   time_of_booking_morning, time_of_booking_night, vehicle_type_premium]]

    # Predict using the model
    prediction = model.predict(input_data)
    
    # Display prediction
    st.write(f"Prediction: {prediction}")
