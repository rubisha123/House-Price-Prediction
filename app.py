import pandas as pd 
import numpy as np
import streamlit as st
import pickle 

with open('model.pk1', 'rb') as f:
  model = pickle.load(f)
with open('sclaer.pk1', 'rb') as f:
   scaler = pickle.load(f)
   
st.title('House Price Prediction')
st.write("""
         This app predicts the **median house value** in California based on the various features!
         """)
st.sidebar.header('User Input Features')

def user_input_features():
    longitude = st.sidebar.slider('Longitude', -124.35, -114.31, -118.49)
    latitude = st.sidebar.slider('Latitude', 32.54, 41.95, 34.26)
    housing_median_age = st.sidebar.slider('Median Age of Houses', 1, 52, 29)
    total_rooms = st.sidebar.slider('Total Rooms', 2, 39320, 2127)
    total_bedrooms = st.sidebar.slider('Total Bedrooms', 1, 6445, 434)
    population = st.sidebar.slider('Population', 3, 35682, 1167)
    households = st.sidebar.slider('Households', 1, 6082, 409)
    median_income = st.sidebar.slider('Median Income ($10,000s)', 0.5, 15.0, 3.54)
    ocean_proximity = st.sidebar.selectbox('Ocean Proximity',                            
         ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'])
    

    rooms_per_household = total_rooms / households
    bedrooms_per_room = total_bedrooms / total_rooms
    population_per_household = population / households
    
    data = {
        'longitude': longitude,
        'latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms,
        'total_bedrooms': total_bedrooms,
        'population': population,
        'households': households,
        'median_income': median_income,
        'rooms_per_household': rooms_per_household,
        'bedrooms_per_room': bedrooms_per_room,
        'population_per_household': population_per_household,
        'ocean_proximity': ocean_proximity
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

ocean_proximity_mapping = {
    '<1H OCEAN': [0, 0, 0, 0],
    'INLAND': [1, 0, 0, 0],
    'ISLAND': [0, 1, 0, 0],
    'NEAR BAY': [0, 0, 1, 0],
    'NEAR OCEAN': [0, 0, 0, 1],
}

encoded = ocean_proximity_mapping[input_df['ocean_proximity'].values[0]]
input_df['ocean_proximity_INLAND'] = encoded[0]
input_df['ocean_proximity_ISLAND'] = encoded[1]
input_df['ocean_proximity_NEAR BAY'] = encoded[2]
input_df['ocean_proximity_NEAR OCEAN'] = encoded[3]

input_df = input_df.drop('ocean_proximity', axis=1)

expected_columns = [
    'longitude', 'latitude', 'housing_median_age', 'total_rooms',
    'total_bedrooms', 'population', 'households', 'median_income',
    'rooms_per_household', 'bedrooms_per_room', 'population_per_household',
    'ocean_proximity_INLAND', 'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY', 'ocean_proximity_NEAR OCEAN'
]
input_df = input_df[expected_columns]

st.subheader('User Input Features')
st.write(input_df)

input_scaled = scaler.transform(input_df)
prediction = model.predict(input_scaled)

st.subheader('Prediction')
st.write(f"Predicted Median House Value: ${prediction[0]:,.2f}")

st.subheader('Location on California Map')
st.map(pd.DataFrame({
    'lat': [input_df['latitude'].values[0]],
    'lon': [input_df['longitude'].values[0]],
}))


    