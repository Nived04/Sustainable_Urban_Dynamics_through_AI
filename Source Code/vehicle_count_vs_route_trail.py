import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('Vehicle_Count_vs_Route.csv')

# Extract data
routes = df['RouteNo']
car_counts = df['Bike']
bike_counts = df['Bus']
bus_counts = df['Car']

# Define the width of the bars
bar_width = 0.25

# Set positions of the bars on the X axis
r1 = range(len(routes))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

fig, ax = plt.subplots(figsize=(10, 10))

ax.bar(r1, car_counts, color='b', width=bar_width, edgecolor='grey', label='Car')
ax.bar(r2, bike_counts, color='g', width=bar_width, edgecolor='grey', label='Bike')
ax.bar(r3, bus_counts, color='r', width=bar_width, edgecolor='grey', label='Bus')

# Add labels
ax.set_xlabel('Route', fontweight='bold')
ax.set_ylabel('Count')
ax.set_title('Vehicle Count by Route')

# Rotate the x-axis labels
plt.xticks([r + bar_width for r in range(len(routes))], routes, rotation=90)

# Reduce the number of ticks
ax.set_xticks([r for i, r in enumerate(r1) if i % 5 == 0])  # Show every 5th label

# Add legend
ax.legend()

# Show plot
plt.tight_layout()
plt.show()