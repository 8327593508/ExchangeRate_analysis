import pandas as pd

forecast_df = pd.read_csv("data/processed/exchange_rate_forecast.csv")

forecast_df["signal"] = "HOLD"

for i in range(1, len(forecast_df)):
    if forecast_df["predicted_rate"].iloc[i] > forecast_df["predicted_rate"].iloc[i-1]:
        forecast_df.at[i, "signal"] = "BUY"
    elif forecast_df["predicted_rate"].iloc[i] < forecast_df["predicted_rate"].iloc[i-1]:
        forecast_df.at[i, "signal"] = "SELL"

forecast_df.to_csv("data/processed/trading_signals.csv", index=False)

print("Trading signals generated successfully!")
