import requests
import pandas as pd
from config.config import API_KEY, BASE_URL, BASE_CURRENCY

def extract_data():
    url = f"{BASE_URL}/{API_KEY}/latest/{BASE_CURRENCY}"
    response = requests.get(url)
    data = response.json()

    print("API Response:", data)   # Debug log

    # Safety check
    if "conversion_rates" not in data:
        raise ValueError(f"API Error: {data}")

    rates = data["conversion_rates"]

    df = pd.DataFrame(list(rates.items()), columns=["currency", "rate"])
    df["base_currency"] = BASE_CURRENCY
    df["date"] = pd.Timestamp.today().date()

    return df

