import numpy as np
import matplotlib.pyplot as plt

# Parameters for the log-normal distribution
mean = 32
sd = 6
size = 100 

def generate_speeds_log_normal(mean, sd, size=1):
    mu = np.log(mean**2 / np.sqrt(sd**2 + mean**2))
    sigma = np.sqrt(np.log(1 + (sd**2 / mean**2)))
    return np.random.lognormal(mu, sigma, size)

bike_speeds = generate_speeds_log_normal(mean, sd, size)

plt.figure(figsize=(10, 6))
plt.hist(bike_speeds, bins=30, alpha=0.7, color='b', density=True)
plt.xlabel('Speed (km/h)')
plt.ylabel('Probability Density')
plt.title('Speed Distribution of Bikes on Route 10')
plt.grid(True)
plt.show()