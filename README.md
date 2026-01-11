

# 📊 Forex Analytics & Trading Intelligence Platform

A full-stack **real-time Forex analytics platform** with automated ETL pipeline, machine learning forecasting, trading signals, user authentication, admin panel, and live dashboard — built using Python, Streamlit, GitHub Actions, and ML.

---

## 🚀 Project Overview

This project is an end-to-end **Forex analytics & trading intelligence system** that:

* Extracts real-time exchange rate data from API
* Cleans & processes data using an automated ETL pipeline
* Trains a machine learning model to forecast exchange rates
* Generates trading signals (BUY / SELL / HOLD)
* Visualizes everything on a live interactive dashboard
* Supports user login, signup, and admin monitoring
* Auto-refreshes data every hour using GitHub Actions
* Deploys online using Streamlit Cloud

It follows **real industry architecture** used in data engineering, analytics, and fintech platforms.

---

## 🧠 System Architecture

```
        ┌────────────┐
        │ Forex API   │
        └─────┬──────┘
              │
         [ ETL Pipeline ]
              │
        ┌─────▼──────┐
        │ Raw Data    │
        └─────┬──────┘
              │
        ┌─────▼──────┐
        │ Clean Data  │
        └─────┬──────┘
              │
        ┌─────▼──────┐
        │ ML Model    │
        └─────┬──────┘
              │
        ┌─────▼──────┐
        │ Forecasts  │
        └─────┬──────┘
              │
        ┌─────▼──────┐
        │ Signals    │
        └─────┬──────┘
              │
        ┌─────▼────────────┐
        │ Streamlit Web App │
        └──────────────────┘
```

---

## 🎯 Key Features

### 🔄 Automated ETL Pipeline

* Extracts real-time exchange rates from ExchangeRate API
* Stores raw and processed datasets
* Cleans and transforms currency data
* Runs automatically every hour using GitHub Actions

### 🤖 Machine Learning Forecasting

* Trains Random Forest regression model
* Uses feature engineering for time-series forecasting
* Predicts next 7-day exchange rate trend
* Stores forecast results automatically

### 📈 Trading Signal Engine

* Generates BUY / SELL / HOLD signals
* Calculates strategy returns
* Computes cumulative profit curve
* Supports trading performance visualization

### 🌐 Live Web Dashboard (Streamlit)

* Real-time market prices
* Multi-currency comparison charts
* Volatility & risk analysis
* Trend indicators
* Forecast visualization
* Trading strategy performance
* Auto-refresh every 60 seconds

### 🔐 Authentication System

* User Signup & Login
* Secure hashed passwords
* Admin panel to view users
* User activity tracking ready

### ⚙ DevOps Automation

* GitHub Actions pipeline runs every hour
* Automatically updates data & forecasts
* Commits new data back to repository
* CI/CD ready

---

## 🖥️ Tech Stack

| Layer      | Technology              |
| ---------- | ----------------------- |
| Backend    | Python                  |
| ETL        | Pandas, Requests        |
| ML         | Scikit-learn, NumPy     |
| Automation | GitHub Actions          |
| Dashboard  | Streamlit, Plotly       |
| Auth       | Streamlit-Authenticator |
| Storage    | CSV (cloud-ready)       |
| Deployment | Streamlit Cloud         |

---

## 📁 Project Structure

```
ExchangeRate_analysis/
│
├── app.py                    # Main Streamlit app
├── signup.py                # User registration
├── auth_utils.py            # Authentication handler
├── run_pipeline.py          # Orchestrates ETL + ML
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── ml/
│   ├── train_model.py
│   ├── predict.py
│   └── trading_signals.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── users.csv
│
├── .github/workflows/
│   └── pipeline.yml         # GitHub Actions automation
│
├── requirements.txt
└── README.md
```

---

## 🔁 Automated Pipeline (GitHub Actions)

* Runs every hour
* Executes ETL pipeline
* Trains ML model
* Generates forecast
* Creates trading signals
* Commits updated data

---

## 📊 Dashboard Capabilities

✔ Live Market Prices
✔ Multi-Currency Comparison
✔ Volatility & Risk Analysis
✔ Trend Direction
✔ 7-Day Forecast
✔ Trading Strategy Performance
✔ User Login & Signup
✔ Admin Panel

---

## 🔐 Authentication

* Secure password hashing
* Signup & Login system
* Admin user management
* Ready for email verification & OTP

---

## 🚀 Deployment

Deployed using **Streamlit Cloud**

* Auto-build from GitHub repo
* Auto-install dependencies
* Auto-deploy on every push

---

## 📌 Future Enhancements

* Email verification system
* Forgot password reset
* Google OAuth login
* User analytics & tracking
* Portfolio simulator
* Trading bot integration
* PostgreSQL backend

---

## 👨‍💻 Author

**Subham Das**
M.Tech Graduate | Data Science & Analytics
Aspiring FinTech / AI Engineer

---

## ⭐ Why This Project Matters

This project demonstrates real-world skills in:

* Data Engineering
* Machine Learning
* DevOps & Automation
* Web Development
* Cloud Deployment
* Security & Authentication
* FinTech Systems

This is not just a dashboard — it's a **full trading intelligence platform**.

---

## 📜 License

MIT License — Free to use, modify and distribute.

---

## 🌟 If you like this project

Give it a ⭐ on GitHub and connect with me on LinkedIn.



Just tell me 👍

