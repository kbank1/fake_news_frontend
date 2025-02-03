import streamlit as st
import requests
import datetime

'''
# Filipe's Taxifare app
'''

'''
### Welcome to my Taxifare app! Here, you will be able to predict the fare of a New York taxi ride
'''

date = st.date_input('Please select a pickup date', datetime.date(2014, 1, 1))
time = st.time_input('Please select a pickup time', datetime.time(10, 00))
pickup_datetime = str(date) + ' ' + str(time)

pickup_longitude = st.number_input('Please select a pickup longitude', value=-73.95)
pickup_latitude = st.number_input('Please select a pickup latitude', value=40.78)
dropoff_longitude = st.number_input('Please select a dropoff longitude', value=-73.98)
dropoff_latitude = st.number_input('Please select a dropoff latitude', value=40.77)

passenger_count = st.slider('Please select the number of passengers', 1, 10, 2)

url = 'https://qonto-973308060059.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = {'pickup_datetime': pickup_datetime,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': passenger_count
        }

response = requests.get(
    url=url,
    params=params,
).json()

st.write(f"Your estimated fare is {round(response['fare'],2)} $USD")
