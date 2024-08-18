import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'C:/Users/Juand/Desktop/Data sc/Data.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-9')

# Data cleaning: I take out the bridge data as im only using the totals
data = data[['Date', 'Day', 'High Temp (°F)', 'Low Temp (°F)', 'Precipitation', 'Total']]

# Convert the total to numeric 
data['Total'] = data['Total'].replace(',', '', regex=True).astype(float)

# Convert precipitation to numeric
data['Precipitation'] = pd.to_numeric(data['Precipitation'], errors='coerce')

# get the average for temperature to make it simpler to graph
data['Average Temp (°F)'] = (data['High Temp (°F)'] + data['Low Temp (°F)']) / 2

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Extract month from the 'Date' column
data['Month'] = data['Date'].dt.strftime('%B')

# get the list of months present in the data
months_present = data['Month'].unique()

# Filter the data to include only April to October
months_of_interest = ['April', 'May', 'June', 'July', 'August', 'September', 'October']
data_filtered = data[data['Month'].isin(months_of_interest)]

# Average Temperature vs. Total Cyclists
plt.figure(figsize=(10, 6))
plt.scatter(data_filtered['Average Temp (°F)'], data_filtered['Total'], color='blue')
plt.title('Effect of Temperature on Total Cyclists')
plt.xlabel('Average Temperature (°F)')
plt.ylabel('Total Cyclists')
plt.grid(True)
plt.show()

# Precipitation vs. Total Cyclists
plt.figure(figsize=(10, 6))
plt.scatter(data_filtered['Precipitation'], data_filtered['Total'], color='green')
plt.title('Effect of Precipitation on Total Cyclists')
plt.xlabel('Precipitation (inches)')
plt.ylabel('Total Cyclists')
plt.grid(True)
plt.show()

# Day of the Week vs. Total Cyclists
plt.figure(figsize=(10, 6))
sns.boxplot(x='Day', y='Total', data=data_filtered, palette='Set2')
plt.title('Day of the Week vs. Total Cyclists')
plt.xlabel('Day of the Week')
plt.ylabel('Total Cyclists')
plt.grid(True)
plt.show()

# Month vs. Total Cyclists
plt.figure(figsize=(10, 6))
sns.boxplot(x='Month', y='Total', data=data_filtered, order=sorted(months_of_interest, key=lambda x: pd.to_datetime(x, format='%B').month), palette='Set3')
plt.title('Month vs. Total Cyclists')
plt.xlabel('Month')
plt.ylabel('Total Cyclists')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
