import streamlit as st
import numpy as np
import pickle
import warnings

warnings.filterwarnings('ignore')

loaded_model = pickle.load(open('air_model.sav', 'rb'))

def check(input_data):
    array_input = np.array(input_data)
    reshaped_input = array_input.reshape(1, -1)
    prediction = loaded_model.predict(reshaped_input)

    if prediction[0] == 0:
        return 'Booking Confirm'
    else:
        return 'Booking not confirm'

def main():
    st.title("Air Booking Prediction")

    num_passengers = st.number_input("Number of Passengers")
    sales_channel = st.number_input("Type of Channel")
    trip_type = st.number_input("Trip Type")
    purchase_lead = st.number_input("Purchase Lead")
    length_of_stay = st.number_input("Length of Stay")
    flight_day = st.number_input("Flight Day")
    route = st.number_input("Route")
    booking_origin = st.number_input("Booking Origin")
    wants_extra_baggage = st.number_input("Extra Baggage")
    wants_preferred_seat = st.number_input("Preferred Seat")
    wants_in_flight_meals = st.number_input("Flight Meals")
    flight_hour_bin = st.number_input("Flight Hour")
    flight_arrival = st.number_input("Flight Arrival")
    flight_duration_scaled = st.number_input("Flight Duration")
    route_frequency_encoded_scaled = st.number_input("Route Frequency")

    pred = ""
    if st.button("Click Here for Booking Confirmation"):
        pred = check([num_passengers, sales_channel, trip_type, purchase_lead, length_of_stay, flight_day, route,
                      booking_origin, wants_extra_baggage, wants_preferred_seat, wants_in_flight_meals,
                      flight_hour_bin, flight_arrival, flight_duration_scaled, route_frequency_encoded_scaled])

    st.success(f"Your Booking Confirmation Chances are: {pred}")

if __name__ == '__main__':
    main()
