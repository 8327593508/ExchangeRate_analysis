import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/raw/exchange_rates_raw.csv")

df["day"] = range(len(df))

X = df[["day"]]
y = df["rate"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "ml/model.pkl")
print("Model trained successfully!")
