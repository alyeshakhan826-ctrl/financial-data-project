# Financial Stock Market Dashboard

## Project Overview

This project analyzes stock market data for five major technology companies during 2024:

- Apple (AAPL)
- Amazon (AMZN)
- Alphabet (GOOGL)
- Microsoft (MSFT)
- NVIDIA (NVDA)

The project demonstrates a complete data analysis workflow:

**Data Collection → Data Cleaning → SQL Database → Analysis → Power BI Dashboard**

## Tools Used

- Python
- Pandas
- yfinance
- SQLite
- SQL
- Power BI

## Data Pipeline

### 1. Data Collection

Historical stock price data was downloaded using Python and Yahoo Finance.

The dataset contains:

- Date
- Ticker
- Close
- High
- Low
- Open
- Volume

### 2. Data Cleaning

The downloaded data was cleaned using Pandas.

The cleaning process included:

- Converting dates to datetime
- Converting numeric columns to appropriate data types
- Checking for missing values
- Checking for duplicate rows
- Verifying the number of records for each stock

The final dataset contains **1,260 rows**, with **252 trading days for each stock**.

### 3. SQL Database

The cleaned data was loaded into a SQLite database.

SQL queries were used to analyze:

- Average closing price
- Trading period
- Starting and ending prices
- 2024 stock returns
- Highest closing prices

### 4. Power BI Dashboard

The final dashboard provides an interactive view of the 2024 stock market data.

The dashboard includes:

- Highest closing price
- Average closing price
- Total trading volume
- 2024 stock returns
- Stock price performance over time
- 2024 return ranking
- Interactive stock selector

## Key Findings

Based on the 2024 dataset:

| Stock | 2024 Return |
|------|------------:|
| AAPL | 35.56% |
| AMZN | 46.33% |
| GOOGL | 37.50% |
| MSFT | 14.50% |
| NVDA | 178.87% |

NVIDIA had the strongest 2024 price return among the five stocks in this dataset.

## Project Structure

```text
financial data project/
│
├── data/
├── database/
├── src/
│   ├── download/
│   ├── clean_stocks.py
│   ├── load_database.py
│   └── query_database.py
│
├── Financial_Stock_Dashboard.pbix
└── README.md