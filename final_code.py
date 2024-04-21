import streamlit as st
import random
import pandas as pd
import joblib
import statistics
# i also need to integrate weather related data
model = joblib.load("regressor.pkl")

def return_actual_pred(prediction, distance):
    if 10 * distance < prediction:
        return prediction
    else:
        return 12.12 * distance

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
estimated_ride_duration = st.number_input("Expected Ride Duration:", value=float(time_in_minutes))
time_of_booking = st.selectbox("Time of Booking:", ["Morning", "Afternoon", "Evening", "Night"])

if time_of_booking == "Morning":
    time_of_booking_morning = 1
    time_of_booking_evening = 0
    time_of_booking_night = 0
elif time_of_booking == "Afternoon":
    time_of_booking_morning = 0
    time_of_booking_evening = 0
    time_of_booking_night = 0
elif time_of_booking == "Evening":
    time_of_booking_morning = 0
    time_of_booking_evening = 1
    time_of_booking_night = 0
elif time_of_booking == "Night":
    time_of_booking_morning = 0
    time_of_booking_evening = 0
    time_of_booking_night = 1

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

drivers_info = []

col1, col2, col3, col4 = st.columns(4)  # Create 4 columns

for i in range(1, 5):  # Generate values for 4 drivers
    number_of_riders = random.randint(55, 75)
    drivers = random.randint(45, 60)
    past_rides = random.randint(1, 100)
    average_ratings = round(random.uniform(1, 5), 2)

    # Store driver information in a dictionary
    driver_info = {
        "Driver": i,
        "Number of Riders": number_of_riders,
        "Drivers": drivers,
        "Past Rides": past_rides,
        "Average Ratings": average_ratings
    }

    # Append the dictionary to the list
    drivers_info.append(driver_info)

    if i == 1:
        with col1:
            st.write(f"Driver {i}:")
            st.write(f"Number of Riders: {number_of_riders}")
            st.write(f"Drivers: {drivers}")
            st.write(f"Past Rides: {past_rides}")
            st.write(f"Average Ratings: {average_ratings}")
            if st.button(f"Predict {i}"):
                input_data = [[number_of_riders, drivers, past_rides, average_ratings,
                               estimated_ride_duration, time_of_booking_evening, time_of_booking_morning,
                               time_of_booking_night, customer_loyalty_status_regular, customer_loyalty_status_silver,
                               location_category_suburban, location_category_urban, time_of_booking_evening,
                               time_of_booking_morning, time_of_booking_night, vehicle_type_premium]]
                prediction = model.predict(input_data)
                prediction_min=return_actual_pred(prediction,distance)
                # st.write(prediction_min)
                rt=number_of_riders/drivers
                # st.write(rt)
                st.write(max(prediction_min*rt,prediction_min))
                
    elif i == 2:
        with col2:
            st.write(f"Driver {i}:")
            st.write(f"Number of Riders: {number_of_riders}")
            st.write(f"Drivers: {drivers}")
            st.write(f"Past Rides: {past_rides}")
            st.write(f"Average Ratings: {average_ratings}")
            if st.button(f"Predict {i}"):
                input_data = [[number_of_riders, drivers, past_rides, average_ratings,
                               estimated_ride_duration, time_of_booking_evening, time_of_booking_morning,
                               time_of_booking_night, customer_loyalty_status_regular, customer_loyalty_status_silver,
                               location_category_suburban, location_category_urban, time_of_booking_evening,
                               time_of_booking_morning, time_of_booking_night, vehicle_type_premium]]
                prediction = model.predict(input_data)
                prediction_min=return_actual_pred(prediction,distance)
                rt=number_of_riders/drivers
                st.write(max(prediction_min*rt,prediction_min))
                
    elif i == 3:
        with col3:
            st.write(f"Driver {i}:")
            st.write(f"Number of Riders: {number_of_riders}")
            st.write(f"Drivers: {drivers}")
            st.write(f"Past Rides: {past_rides}")
            st.write(f"Average Ratings: {average_ratings}")
            if st.button(f"Predict {i}"):
                input_data = [[number_of_riders, drivers, past_rides, average_ratings,
                               estimated_ride_duration, time_of_booking_evening, time_of_booking_morning,
                               time_of_booking_night, customer_loyalty_status_regular, customer_loyalty_status_silver,
                               location_category_suburban, location_category_urban, time_of_booking_evening,
                               time_of_booking_morning, time_of_booking_night, vehicle_type_premium]]
                prediction = model.predict(input_data)
                prediction_min=return_actual_pred(prediction,distance)
                rt=number_of_riders/drivers
                st.write(max(prediction_min*rt,prediction_min))
    elif i == 4:
        with col4:
            st.write(f"Driver {i}:")
            st.write(f"Number of Riders: {number_of_riders}")
            st.write(f"Drivers: {drivers}")
            st.write(f"Past Rides: {past_rides}")
            st.write(f"Average Ratings: {average_ratings}")
            if st.button(f"Predict {i}"):
                input_data = [[number_of_riders, drivers, past_rides, average_ratings,
                               estimated_ride_duration, time_of_booking_evening, time_of_booking_morning,
                               time_of_booking_night, customer_loyalty_status_regular, customer_loyalty_status_silver,
                               location_category_suburban, location_category_urban, time_of_booking_evening,
                               time_of_booking_morning, time_of_booking_night, vehicle_type_premium]]
                prediction = model.predict(input_data)
                prediction_min=return_actual_pred(prediction,distance)
                rt=number_of_riders/drivers
                st.write(max(prediction_min*rt,prediction_min))
