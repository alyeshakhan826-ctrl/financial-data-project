import yfinance as yf

data = yf.download("AAPL", start="2024-01-01", end="2025-01-01")

data.to_csv("data/aapl_2024_raw.csv")

print("Data downloaded and saved successfully!")
print(data.head())