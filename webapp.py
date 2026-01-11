import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------- Page Config ----------------
st.set_page_config(page_title="Forex Analytics Platform", layout="wide")

# Auto refresh every 60 seconds
st_autorefresh(interval=60 * 1000, key="data_refresh")

# ---------------- Load Data ----------------
actual_df = pd.read_csv("data/processed/exchange_rates_clean.csv")
forecast_df = pd.read_csv("data/processed/exchange_rate_forecast.csv")
signals_df = pd.read_csv("data/processed/trading_signals.csv")

actual_df["date"] = pd.to_datetime(actual_df["date"])
forecast_df["date"] = pd.to_datetime(forecast_df["date"])

# ---------------- Sidebar ----------------
st.sidebar.title("Currency Selector")

currency_list = actual_df["currency"].unique().tolist()
selected_currencies = st.sidebar.multiselect(
    "Select currencies for comparison",
    currency_list,
    default=currency_list[:3]
)

# ---------------- Title ----------------
st.title("💱 Forex Analytics & Trading Intelligence Platform")

# ---------------- KPI Panel ----------------
latest_data = actual_df.sort_values("date").groupby("currency").last().reset_index()
kpi_df = latest_data[latest_data["currency"].isin(selected_currencies)]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Currencies Tracked", len(currency_list))

with col2:
    avg_rate = round(kpi_df["rate"].mean(), 4)
    st.metric("Avg Selected Rate", avg_rate)

with col3:
    latest_date = actual_df["date"].max().date()
    st.metric("Last Update", latest_date.strftime("%Y-%m-%d"))

st.divider()

# ---------------- Multi-Currency Comparison ----------------
st.subheader("📊 Multi-Currency Comparison")

compare_df = actual_df[actual_df["currency"].isin(selected_currencies)]

fig_compare = px.line(
    compare_df,
    x="date",
    y="rate",
    color="currency",
    title="Exchange Rate Comparison"
)

st.plotly_chart(fig_compare, use_container_width=True)

st.divider()

# ---------------- Volatility Analysis ----------------
st.subheader("⚡ Volatility & Risk Analysis")

volatility_df = compare_df.copy()
volatility_df["daily_return"] = volatility_df.groupby("currency")["rate"].pct_change()

volatility_summary = volatility_df.groupby("currency")["daily_return"].std().reset_index()
volatility_summary["volatility"] = volatility_summary["daily_return"] * 100

st.dataframe(
    volatility_summary[["currency", "volatility"]]
    .rename(columns={"volatility": "Volatility %"})
)

fig_vol = px.bar(
    volatility_summary,
    x="currency",
    y="volatility",
    title="Currency Volatility (%)"
)

st.plotly_chart(fig_vol, use_container_width=True)

st.divider()

# ---------------- Trend Direction ----------------
st.subheader("📈 Trend Direction Indicator")

trend_list = []

for currency in selected_currencies:
    temp = compare_df[compare_df["currency"] == currency].sort_values("date").tail(2)

    if len(temp) == 2:
        if temp.iloc[-1]["rate"] > temp.iloc[-2]["rate"]:
            trend = "📈 Uptrend"
        elif temp.iloc[-1]["rate"] < temp.iloc[-2]["rate"]:
            trend = "📉 Downtrend"
        else:
            trend = "➡ Sideways"

        trend_list.append([currency, trend])

trend_df = pd.DataFrame(trend_list, columns=["Currency", "Trend"])
st.dataframe(trend_df)

st.divider()

# ---------------- Forecast ----------------
st.subheader("🔮 7-Day Forecast")

fig_forecast = px.line(
    forecast_df,
    x="date",
    y="predicted_rate",
    title="Exchange Rate Forecast"
)

st.plotly_chart(fig_forecast, use_container_width=True)

st.divider()

# ---------------- Trading Strategy Performance ----------------
st.subheader("💰 Trading Strategy Performance")

signals_df["return"] = signals_df["predicted_rate"].pct_change()

signals_df["strategy_return"] = np.where(
    signals_df["signal"] == "BUY",
    signals_df["return"],
    np.where(signals_df["signal"] == "SELL", -signals_df["return"], 0)
)

signals_df["cumulative_return"] = (1 + signals_df["strategy_return"]).cumprod()

fig_strategy = px.line(
    signals_df,
    x="date",
    y="cumulative_return",
    title="Trading Strategy Performance"
)

st.plotly_chart(fig_strategy, use_container_width=True)

st.dataframe(signals_df)

st.success("Dashboard auto-updated from live pipeline data!")
