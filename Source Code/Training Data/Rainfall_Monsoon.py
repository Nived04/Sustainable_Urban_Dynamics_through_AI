import numpy as np
import pandas as pd
import scipy.stats as stats
from datetime import timedelta, datetime
import matplotlib.pyplot as plt

# Gamma distribution parameters
alpha = 2.0

daily_rain_prob = {
    "May": (0.3, 0,3),
    "June": (0.5, 0.5), 
    "July": (0.8, 0.8),
    "August": (0.6, 0.5),
    "September": (0.6, 0.7),
    "October": (0.3, 0.3)
}

start_date = datetime(2022, 5, 25)
end_date = datetime(2022, 10, 7)
date_range = pd.date_range(start_date, end_date)

def sample_zero_inflated_gamma(p_rain, alpha, beta, size=1):
    rain_occurence = np.random.binomial(1, p_rain, size)
    gamma_samples = stats.gamma(a=alpha, scale=beta).rvs(size)
    return rain_occurence*gamma_samples

daily_rainfall = []

for date in date_range:
    month = date.strftime('%B')
    p_rain = daily_rain_prob[month][0]
    beta = 2.5*daily_rain_prob[month][1]
    rainfall = sample_zero_inflated_gamma(p_rain, alpha, beta)
    daily_rainfall.append((date.strftime('%Y-%m-%d'), rainfall[0]))

# Create a DataFrame and save to CSV
df = pd.DataFrame(daily_rainfall, columns=['Date', 'Rainfall (mm)'])
df.to_csv('daily_rainfall_may_october.csv', index=False)

plt.figure(figsize=(15, 6))
plt.plot(pd.to_datetime(df['Date']), df['Rainfall (mm)'], marker='o', linestyle='-', markersize=3)
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')
plt.title('Simulated Daily Rainfall from May 25 to October 7')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()