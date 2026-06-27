import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Weather Scraping Dashboard")
st.write("This dashboard shows scraped weather data by city.")

# Import data from the weather database
conn = sqlite3.connect("weather.db")
df = pd.read_sql_query("SELECT * FROM weather_clean", conn)
conn.close()

# Clean the temperature data for visualization
df["temperature"] = df["temperature"].str.replace("°F", "", regex=False)
df["temperature"] = df["temperature"].str.strip()
df["temperature"] = df["temperature"].astype(float)

# Display the weather data
st.subheader("Weather Data")
st.dataframe(df)

# Add a city filter for user interaction
st.sidebar.header("Filter Options")
selected_city = st.sidebar.selectbox("Select a city", sorted(df["city"].unique()))

filtered_df = df[df["city"] == selected_city]

st.subheader("Selected City")
st.write(filtered_df)

# Visualization 1: Temperature by city
st.subheader("Temperature by City")
bar_chart = px.bar(
    df,
    x="city",
    y="temperature",
    title="Temperature by City"
)
st.plotly_chart(bar_chart)

# Visualization 2: Temperature distribution
st.subheader("Temperature Distribution")
histogram = px.histogram(
    df,
    x="temperature",
    title="Temperature Distribution"
)
st.plotly_chart(histogram)

# Visualization 3: Temperature scatter plot
st.subheader("Temperature Scatter Plot")
scatter_chart = px.scatter(
    df,
    x="city",
    y="temperature",
    title="Temperature Scatter Plot"
)
st.plotly_chart(scatter_chart)