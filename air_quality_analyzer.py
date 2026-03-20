# Air Quality Data Analyzer System - Advanced Version
# Developed in Python

import pandas as pd
import matplotlib.pyplot as plt

# Load data (CSV file containing air quality data)
file_path = "air_quality_data.csv"

try:
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()  # 👈 Fix: removes any spaces in column names
    print("\n✅ Data loaded successfully!\n")
except FileNotFoundError:
    print("⚠️ File not found! Please check your CSV file name/path.")
    exit()

# Display sample data
print("📋 Sample Data:\n", data.head())

# Calculate average pollutant levels
print("\n📊 Average Pollutant Levels:")
average_values = data[['PM2.5', 'PM10', 'NO2', 'CO', 'O3']].mean()
print(average_values)

# Determine air quality based on PM2.5
def air_quality_index(pm25):
    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Moderate"
    elif pm25 <= 200:
        return "Unhealthy"
    else:
        return "Hazardous"

# Add air quality category
data['Air_Quality'] = data['PM2.5'].apply(air_quality_index)

# Show results
print("\n🌫️ Air Quality Category per City:")
print(data[['City', 'PM2.5', 'Air_Quality']])

# Sort for top cleanest and most polluted
cleanest = data.sort_values(by='PM2.5', ascending=True).head(5)
polluted = data.sort_values(by='PM2.5', ascending=False).head(5)

print("\n🌿 Top 5 Cleanest Cities:")
print(cleanest[['City', 'PM2.5']])

print("\n🔥 Top 5 Most Polluted Cities:")
print(polluted[['City', 'PM2.5']])

# --- Plot 1: Bar chart for pollutant levels ---
plt.figure(figsize=(10,6))
data.plot(x='City', y=['PM2.5','PM10','NO2','CO','O3'], kind='bar')
plt.title("Air Quality Data Analysis by City")
plt.xlabel("City")
plt.ylabel("Pollutant Levels (µg/m³)")
plt.grid(True)
plt.tight_layout()
plt.show(block=False)
plt.pause(2)   # keeps the window open for 2 seconds before next plot


# --- Plot 2: Pie chart for air quality categories ---
category_counts = data['Air_Quality'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Air Quality Category Distribution")
plt.show()

# Save analyzed data
data.to_csv("analyzed_air_quality.csv", index=False)
print("\n💾 Results saved to 'analyzed_air_quality.csv'")
