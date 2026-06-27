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
df["tempera