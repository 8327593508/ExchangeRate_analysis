import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Load processed data
df = pd.read_csv("data/processed/exchange_rates_clean.csv")

print("Initial data shape:", df.shape)

# Sort by date
df = df.sort_values("date")

# Create lag features
df["lag_1"] = df["rate"].shift(1)
df["lag_2"] = df["rate"].shift(2)
df["lag_3"] = df["rate"].shift(3)

# Create rolling average
df["rolling_mean_3"] = df["rate"].rolling(window=3).mean()

# Remove NaN rows
df = df.dropna()

print("Data shape after feature engineering:", df.shape)

# Safety check
if len(df) < 5:
    raise ValueError("Not enough historical data. Run ETL for more days to collect data.")

# Features and target
X = df[["lag_1", "lag_2", "lag_3", "rolling_mean_3"]]
y = df["rate"]

# Train-test split
split = int(len(df) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nModel Performance:")
print("MAE:", mae)
print("RMSE:", rmse)

# Save model
joblib.dump(model, "ml/model.pkl")

print("\nModel trained and saved successfully!")

