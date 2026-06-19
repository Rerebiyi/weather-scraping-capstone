from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the browser
driver = webdriver.Chrome()

# Open the weather website
url = "https://www.timeanddate.com/weather/"
driver.get(url)

# Give the page time to load
time.sleep(3)

# Find all table cells
cells = driver.find_elements(By.TAG_NAME, "td")

weather_data = []

# Each weather record uses 4 cells: city, local time, blank/icon, temperature
for i in range(0, len(cells), 4):
    try:
        city = cells[i].text
        local_time = cells[i + 1].text
        temperature = cells[i + 3].text

        if city != "" and local_time != "" and temperature != "":
            weather_data.append({
                "city": city,
                "local_time": local_time,
                "temperature": temperature
            })

    except IndexError:
        print("Skipping incomplete row")

# Close the browser
driver.quit()

# Create a DataFrame
df = pd.DataFrame(weather_data)

# Save raw scraped data
df.to_csv("data/weather_raw.csv", index=False)

# Show rows before cleaning
print("Rows before cleaning:", len(df))

# Remove duplicate rows
df = df.drop_duplicates()

# Check for missing values
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

# Show rows after cleaning
print("Rows after cleaning:", len(df))

# Clean city names
df["city"] = df["city"].str.replace("*", "", regex=False).str.strip()

# Save data to CSV
df.to_csv("data/weather_clean.csv", index=False)

print("Scraping complete")
print(df.head())
print("Rows saved:", len(df))