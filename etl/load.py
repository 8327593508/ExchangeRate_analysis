import os
import pandas as pd

def load_data(df):
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    raw_file = "data/raw/exchange_rates_raw.csv"
    processed_file = "data/processed/exchange_rates_clean.csv"

    # If file exists, append
    if os.path.exists(raw_file):
        old_df = pd.read_csv(raw_file)
        df = pd.concat([old_df, df], ignore_index=True)

    # Remove duplicates (same currency + same date)
    df = df.drop_duplicates(subset=["currency", "date"])

    # Save raw
    df.to_csv(raw_file, index=False)

    # Save processed
    df.to_csv(processed_file, index=False)

    print("Data appended successfully!")

