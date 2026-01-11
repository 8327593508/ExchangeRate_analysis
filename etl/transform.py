def transform_data(df):
    df = df.dropna()
    df["rate"] = df["rate"].astype(float)
    return df
