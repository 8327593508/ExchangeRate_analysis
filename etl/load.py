import os

def load_data(df):
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/exchange_rates_raw.csv", index=False)
