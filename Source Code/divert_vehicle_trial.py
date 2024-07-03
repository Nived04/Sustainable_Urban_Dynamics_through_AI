import random
import pandas as pd

#same data
df = pd.read_csv('Vehicle_Count_vs_Route.csv')

total_routes = len(df.index)
routes = df['RouteNo'].tolist() # extraced routes
random.shuffle(routes) # shuffle the routes

group_size = 25
groups = [routes[i * group_size:(i + 1) * group_size] for i in range(5)]

# initially 0 vehicle count in the five groups
vehicle_counts = {
    'Car': [0]*5,
    'Bike': [0]*5,
    'Bus': [0]*5
}

for i, group in enumerate(groups):
    for route in group:
        vehicle_counts['Car'][i] += df[df['RouteNo'] == route]['Car'].values[0]
        vehicle_counts['Bike'][i] += df[df['RouteNo'] == route]['Bike'].values[0]
        vehicle_counts['Bus'][i] += df[df['RouteNo'] == route]['Bus'].values[0]

bike_weight = 1.0
car_weight_range = (1.18, 1.22)
bus_weight_range = (1.45, 1.55)

weights = {
    'Bike': [bike_weight]*5,
    'Car': [],
    'Bus': []
}

for _ in range(5):
    car_weight = round(random.uniform(*car_weight_range), 2)
    bus_weight = round(random.uniform(*bus_weight_range), 2)
    weights['Car'].append(car_weight)
    weights['Bus'].append(bus_weight)

matrix = []
for i in range(5):
    row = []
    for vehicle_type in vehicle_counts:
        count = vehicle_counts[vehicle_type][i]
        weight = weights[vehicle_type][i]
        row.append(count*weight) 
    matrix.append(row)
    
def divert_vehicle(vehicle_type, matrix):
    min_value = float('inf')
    best_group = -1
    for i in range(len(matrix)):
        if matrix[vehicle_type][i] < min_value:
            min_value = matrix[vehicle_type][i]
            best_group = i + 1  # Adding 1 to make it 1-indexed
    return best_group

incoming_vehicle = random.choice(['Car', 'Bike', 'Bus'])

assigned_group = divert_vehicle(incoming_vehicle, matrix)

print(f"Incoming {incoming_vehicle} diverted to Group {assigned_group}")