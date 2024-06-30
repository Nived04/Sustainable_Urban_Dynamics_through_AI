import itertools
import random
import csv

# Sample data of 2500 latitude-longitude addresses
sample_addresses = [
    (40.712776, -74.005974),  # Example: New York City
    # Add more addresses here...
]

# Generate all possible pairs of addresses
address_pairs = list(itertools.permutations(sample_addresses, 2))

# Generate random routes
routes = []
route_no = 1
for _ in range(50000):
    num_stops = random.randint(2, min(20, len(sample_addresses) - 1))
    selected_stops = random.sample(sample_addresses, num_stops)
    selected_stops.append(selected_stops[0])  # Ensure loop back to the starting point

    route_details = []
    for seq_no in range(num_stops):
        route_details.append((route_no, seq_no + 1, selected_stops[seq_no], selected_stops[seq_no + 1]))

    routes.extend(route_details)
    route_no += 1

# Write routes to a CSV file
csv_file = 'routes.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['RouteNo', 'SeqNo', 'StartLat', 'StartLong', 'EndLat', 'EndLong'])
    writer.writerows(routes)

print(f"Routes saved to {csv_file}")