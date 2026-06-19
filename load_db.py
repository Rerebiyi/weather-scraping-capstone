import sqlite3
import pandas as pd

# Load CSV files
raw_df = pd.read_csv("data/weather_raw.csv")
clean_df = pd.read_csv("data/weather_clean.csv")

# Create SQLite database connection
conn = sqlite3.connect("weather.db")

# Import raw weather data
raw_df.to_sql("weather_raw", conn, if_exists="replace", index=False)

# Import cleaned weather data
clean_df.to_sql("weather_clean", conn, if_exists="replace", index=False)
# Verify row counts in database tables
raw_count = pd.read_sql_query(
    "SELECT COUNT(*) AS count FROM weather_raw",
    conn
)

clean_count = pd.read_sql_query(
    "SELECT COUNT(*) AS count FROM weather_clean",
    conn
)

print("\nWeather Raw Table:")
print(raw_count)

print("\nWeather Clean Table:")
print(clean_count)

# Close connection
conn.close()

print("Weather data saved to SQLite database.")