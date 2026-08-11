import yfinance as yf
import pandas as pd

# Stocks we want to analyze
tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL"]

# Download data
data = yf.download(
    tickers,
    start="2024-01-01",
    end="2025-01-01",
    group_by="ticker"
)

# Create an empty list
all_stocks = []

# Process each stock
for ticker in tickers:
    stock = data[ticker].copy()

    # Turn Date from the index into a normal column
    stock.reset_index(inplace=True)

    # Add ticker/company identifier
    stock["Ticker"] = ticker

    # Keep only the columns we need
    stock = stock[
        ["Date", "Ticker", "Close", "High", "Low", "Open", "Volume"]
    ]

    all_stocks.append(stock)

# Combine all stocks
combined_data = pd.concat(all_stocks, ignore_index=True)

# Save raw data
combined_data.to_csv(
    "data/stocks_2024_raw.csv",
    index=False
)

print("Stock data downloaded successfully!")
print(combined_data.head())

print("\nShape:")
print(combined_data.shape)