import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.header('Comparing Price and Days of car listings from 2018')
st.markdown("This is a web app to explore different variables and their relation to length of a car listing and price for vehicles from a 2018 car listing dataset of 14,000 cars.")

# Setting the listed_cars variable to the entire dataset and calling some basic methods to better understand the data.
listed_cars=pd.read_csv('../datasets/vehicles_us.csv') # Dataset from listed vehicles being sold in the US
# Setting Graph Figure for plotly objects
fig = go.Figure()
# Formatting date posted to datetime so it may be easier to handle later. Might remove if I never use it.
listed_cars['date_posted'] = pd.to_datetime(listed_cars['date_posted'], format='%Y-%m-%d')

# Creating a clean dataFrame with the null values completely removed
cleanDF = listed_cars.dropna(axis=0, how='any')

# Converting to formats
cleanDF['is_4wd'] = cleanDF['is_4wd'].astype('bool')
cleanDF['model_year'] = cleanDF['model_year'].astype('int')
cleanDF['cylinders'] = cleanDF['cylinders'].astype('int')
cleanDF['price'] = round(cleanDF['price'].astype('float'),2)
# Pulling just the columns for the histograms I want to use
hist_data = cleanDF[['price', 'model_year', 'model', 'type', 'condition', 'odometer', 'days_listed']]
# Choices of X values user can choose from with the interactive histograms
x_choices = ['type', 'model', 'model_year', 'condition', 'odometer']
# One select-box for which variable to look at
x_var = st.selectbox('Select X axis variable:', options=x_choices)
price_fig = px.histogram(hist_data, x=x_var, y='price', histfunc='avg', title='Price')
st.plotly_chart(price_fig, use_container_width=True)
days_fig = px.histogram(hist_data, x=x_var, y='days_listed', histfunc='avg', title='Days Listed')
st.plotly_chart(days_fig, use_container_width=True)