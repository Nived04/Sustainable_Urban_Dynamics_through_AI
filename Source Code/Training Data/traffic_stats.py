import numpy as np
import pandas as pd
from scipy.stats import truncnorm

major_roads = [101, 201, 301]  # Major roads
other_major_roads = list(range(10, 301, 10))  # Other major roads in multiples of 10
small_roads = list(set(range(1, 301)) - set(major_roads) - set(other_major_roads))

# Vehicle types and their speed parameters (mean and standard deviation)
speed_params = {
    "bikes": {
        "major_roads": (45, 3),
        "other_major_roads": (35, 3),
        "small_roads": (25, 3)
    },
    "cars": {
        "major_roads": (50, 5),
        "other_major_roads": (32, 3),
        "small_roads": (23, 3)
    },
    "buses": {
        "major_roads": (40, 2),
        "other_major_roads": (30, 2),
        "small_roads": (30, 1)
    }
}

# Function to generate log-normal distribution data
def generate_speeds(mean, sd, lower=0, upper=70, size=1):
    return truncnorm(
        (lower - mean) / sd, (upper - mean) / sd, loc=mean, scale=sd).rvs(size)

# Generate speed data for 300 roads
num_roads = 301
speed_data = []

for road in range(1, num_roads + 1):
    if road in major_roads:
        road_type = "major_roads"
    elif road in other_major_roads:
        road_type = "other_major_roads"
    else:
        road_type = "small_roads"
    
    # Initialize speeds for each vehicle type
    bike_speed = generate_speeds(*speed_params["bikes"][road_type], size=1)[0]
    car_speed = generate_speeds(*speed_params["cars"][road_type], size=1)[0]
    bus_speed = generate_speeds(*speed_params["buses"][road_type], size=1)[0]
    
    speed_data.append((road, bike_speed, car_speed, bus_speed))

df_speeds = pd.DataFrame(speed_data, columns=['Road_ID', 'Bike_Speed_kmph', 'Car_Speed_kmph', 'Bus_Speed_kmph'])
df_speeds.to_csv('average_speeds_on_city_roads.csv', index=False)
