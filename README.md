

# 📊 Forex Analytics & Trading Intelligence Platform

A full-stack **real-time Forex analytics platform** with automated ETL pipeline, machine learning forecasting, trading signals, authentication system, admin panel, and live dashboard — built using Python, Streamlit, GitHub Actions, and ML.

---

## 🌐 Live Dashboard (Real-Time Web App)

🔴 **Live Forex Analytics Platform**
👉 **Access Dashboard:**
[https://webapppy-okwrqvknvcnxgc6fhegude.streamlit.app/](https://webapppy-okwrqvknvcnxgc6fhegude.streamlit.app/)

The dashboard updates automatically with:

* Real-time exchange rates
* Machine learning forecasts
* Trading signals
* Strategy performance
* Volatility & trend analysis

Auto-refreshes every 60 seconds and pulls new data every hour via GitHub Actions.

---

## 🚀 Project Overview

This project is a complete **Forex trading intelligence system** that performs:

* Real-time API data extraction
* Automated ETL processing
* Machine learning forecasting
* Trading signal generation
* Live analytics dashboard
* Secure user login & signup
* Admin monitoring
* Cloud deployment
* CI/CD automation

It follows real-world **FinTech & Data Engineering architecture**.

---

## 🧠 System Architecture

```
Forex API
   │
   ▼
ETL Pipeline (Extract → Transform → Load)
   │
   ▼
Clean Dataset
   │
   ▼
Machine Learning Model
   │
   ▼
Forecast Engine
   │
   ▼
Trading Signal Generator
   │
   ▼
Streamlit Web Dashboard
   │
   ▼
Users (Login / Signup / Admin)
```

---

## 🎯 Core Features

### 🔄 Automated ETL Pipeline

* Extracts real-time exchange rates from ExchangeRate API
* Cleans and transforms raw data
* Stores raw and processed datasets
* Runs every hour using GitHub Actions

### 🤖 Machine Learning Forecasting

* Trains Random Forest regression model
* Uses time-series features
* Predicts next 7-day exchange rate trend
* Stores forecast results automatically

### 📈 Trading Signal Engine

* Generates BUY / SELL / HOLD signals
* Calculates strategy returns
* Computes cumulative profit curve

### 🌐 Live Web Dashboard

* Real-time market prices
* Multi-currency comparison
* Volatility & risk analysis
* Trend indicators
* Forecast visualization
* Trading performance tracking
* Auto-refresh every 60 seconds

### 🔐 Authentication System

* User Signup & Login
* Secure hashed passwords
* Admin panel to view all users

### ⚙ DevOps Automation

* GitHub Actions pipeline runs hourly
* Automatically updates datasets
* Retrains ML model
* Generates forecasts & signals
* Commits updated data

---

## 📁 Project Structure

```
ExchangeRate_analysis/
│
├── app.py                    # Main Streamlit web application
├── signup.py                # User registration page
├── auth_utils.py            # Authentication loader
├── run_pipeline.py          # Pipeline orchestrator
│
├── etl/
│   ├── extract.py           # API extraction
│   ├── transform.py         # Data cleaning
│   └── load.py              # Data storage
│
├── ml/
│   ├── train_model.py       # Model training
│   ├── predict.py           # Forecast generation
│   └── trading_signals.py  # Trading signal engine
│
├── data/
│   ├── raw/                # Raw API data
│   ├── processed/          # Cleaned data & forecasts
│   └── users.csv           # User database
│
├── .github/workflows/
│   └── pipeline.yml        # GitHub Actions automation
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Local Setup & Installation

### Step 1 — Clone repository

```bash
git clone https://github.com/yourusername/ExchangeRate_analysis.git
cd ExchangeRate_analysis
```

### Step 2 — Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Add API Key

Edit `app.py`:

```python
API_KEY = "your_api_key_here"
```

---

## ▶ Run Pipeline Locally

```bash
python run_pipeline.py
```

This will:

* Fetch latest exchange rates
* Clean data
* Train ML model
* Generate forecasts
* Generate trading signals

---

## ▶ Run Web App Locally

```bash
streamlit run app.py
```

Access:

```
http://localhost:8501
```

---

## 🔐 User Authentication

### Signup

* Create account using signup page
* Passwords are hashed and stored securely

### Login

* Access dashboard after authentication

### Admin Panel

* Login as admin
* View registered users

---

## 🔁 Automated Pipeline (CI/CD)

GitHub Actions runs every hour:

* Executes ETL pipeline
* Retrains ML model
* Updates forecasts
* Generates trading signals
* Pushes updated data to repository

---

## ☁ Deployment

Deployed using **Streamlit Cloud**

* Auto-build from GitHub repo
* Auto-install dependencies
* Auto-deploy on every push

---

## 📌 Future Enhancements

* Email verification
* Forgot password
* Google OAuth login
* Portfolio simulator
* Trading bot integration
* PostgreSQL backend
* User analytics

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



Just tell me 👍
