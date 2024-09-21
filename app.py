import os
import pandas as pd
import streamlit as st
import plotly.express as px



def load_data():
    # Determine the base path of the current script
    base_path = os.path.dirname(__file__)

    # Construct the relative file path
    file_path = os.path.join(base_path, 'vehicles_us.csv')
    
    # Print current working directory and list files for debugging
    print(f"Current working directory: {os.getcwd()}")
    print(f"Listing files in the directory: {os.listdir(os.getcwd())}")
    print(f"Loading data from: {file_path}")

    # Load the CSV data
    df = pd.read_csv(file_path)

    # Handle missing values
    df['model_year'] = df['model_year'].fillna(df['model_year'].median())
    df['cylinders'] = df.groupby('model')['cylinders'].apply(lambda x: x.fillna(x.median()))
    df['odometer'] = df.groupby('model')['odometer'].apply(lambda x: x.fillna(x.median()))
    df['paint_color'] = df['paint_color'].fillna('Unknown')
    
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
