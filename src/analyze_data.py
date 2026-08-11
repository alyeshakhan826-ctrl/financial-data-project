import pandas as pd

# Load cleaned data
data = pd.read_csv("data/aapl_2024_clean.csv")

# Convert Date back to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Basic statistics
print("BASIC STATISTICS:")
print(data.describe())

# Calculate daily percentage return
data["Daily_Return"] = data["Close"].pct_change() * 100

print("\nDAILY RETURNS:")
print(data[["Date", "Close", "Daily_Return"]].head(10))

print("\nRETURN STATISTICS:")
print(data["Daily_Return"].describe())

# Calculate total return
starting_price = data["Close"].iloc[0]
ending_price = data["Close"].iloc[-1]

total_return = (ending_price / starting_price - 1) * 100

print("\nTOTAL RETURN:")
print(f"Starting price: ${starting_price:.2f}")
print(f"Ending price: ${ending_price:.2f}")
print(f"Total return: {total_return:.2f}%")

# Best trading day
best_day = data.loc[data["Daily_Return"].idxmax()]

# Worst trading day
worst_day = data.loc[data["Daily_Return"].idxmin()]

# Highest volume day
highest_volume_day = data.loc[data["Volume"].idxmax()]

print("\nBEST TRADING DAY:")
print(f"Date: {best_day['Date'].date()}")
print(f"Return: {best_day['Daily_Return']:.2f}%")

print("\nWORST TRADING DAY:")
print(f"Date: {worst_day['Date'].date()}")
print(f"Return: {worst_day['Daily_Return']:.2f}%")

print("\nHIGHEST VOLUME DAY:")
print(f"Date: {highest_volume_day['Date'].date()}")
print(f"Volume: {highest_volume_day['Volume']:,.0f}")