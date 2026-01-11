import pandas as pd
import joblib
from datetime import timedelta

# Load processed data
df = pd.read_csv("data/processed/exchange_rates_clean.csv")

# Filter INR currency
df = df.sort_values("date")

# Safety check
if len(df) < 5:
    raise ValueError("Not enough historical data for prediction. Run ETL for more days.")

# Create features
df["lag_1"] = df["rate"].shift(1)
df["lag_2"] = df["rate"].shift(2)
df["lag_3"] = df["rate"].shift(3)
df["rolling_mean_3"] = df["rate"].rolling(window=3).mean()
df = df.dropna()

# Load trained model
model = joblib.load("ml/model.pkl")

# Get last known values
last_rates = df["rate"].tail(3).values

lag_1 = last_rates[2]
lag_2 = last_rates[1]
lag_3 = last_rates[0]
rolling_mean = last_rates.mean()

future_dates = []
future_rates = []

current_date = pd.to_datetime(df.iloc[-1]["date"])

for i in range(7):
    X_future = pd.DataFrame([{
        "lag_1": lag_1,
        "lag_2": lag_2,
        "lag_3": lag_3,
        "rolling_mean_3": rolling_mean
    }])

    prediction = model.predict(X_future)[0]

    current_date += timedelta(days=1)
    future_dates.append(current_date.date())
    future_rates.append(round(prediction, 4))

    # Update lags
    lag_3 = lag_2
    lag_2 = lag_1
    lag_1 = prediction
    rolling_mean = (lag_1 + lag_2 + lag_3) / 3

# Save forecast
forecast_df = pd.DataFrame({
    "date": future_dates,
    "predicted_rate": future_rates
})

forecast_df.to_csv("data/processed/exchange_rate_forecast.csv", index=False)

print("7-day forecast generated successfully!")

