import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate fake historical USD-INR data for last 30 days
start_date = datetime.today() - timedelta(days=30)
dates = [start_date + timedelta(days=i) for i in range(30)]

rates = []
base_rate = 83

for i in range(30):
    fluctuation = np.random.uniform(-0.3, 0.3)
    rates.append(round(base_rate + fluctuation + i*0.01, 2))

df = pd.DataFrame({
    "currency": ["INR"] * 30,
    "rate": rates,
    "base_currency": ["USD"] * 30,
    "date": [d.date() for d in dates]
})

# Save to processed file
df.to_csv("data/processed/exchange_rates_clean.csv", index=False)

print("Historical data generated successfully!")
