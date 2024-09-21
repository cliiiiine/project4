import os
import pandas as pd
import streamlit as st
import plotly.express as px



def load_data():
    file_path = '/Users/keithrobinson/Desktop/TripleTen/Projects//project4/vehicles_us.csv'
    print(f"Loading data from: {file_path}")
    
    df = pd.read_csv('/Users/keithrobinson/Desktop/TripleTen/Projects/project4/vehicles_us.csv')

    return df

data = load_data()

st.header('Exploratory Data Analysis for Vehicles Dataset')

st.subheader('Histogram of Vehicle Prices')
fig_hist = px.histogram(data, x='price', nbins=30, title='Distribution of Vehicle Prices')
st.plotly_chart(fig_hist)

st.subheader("Scatter Plot: Odometer vs. Price")
fig_scatter = px.scatter(data, x='odometer', y='price', color='type', title='Odometer vs. Price for Different Vehicle Types')
st.plotly_chart(fig_scatter)

if st.checkbox('Show Histogram of Odometer Readings'):
    st.subheader('Histogram of Odometer Readings')
    fig_odo_hist = px.histogram(data, x='odometer', nbins=30, title='Distribution of Odometer Readings')
    st.plotly_chart(fig_odo_hist)