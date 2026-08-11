import pandas as pd

# Load raw stock data
data = pd.read_csv("data/stocks_2024_raw.csv")

# Convert Date to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Make sure numeric columns are numeric
numeric_columns = ["Close", "High", "Low", "Open", "Volume"]

for column in numeric_columns:
    data[column] = pd.to_numeric(data[column], errors="coerce")

# Remove rows with missing values
data.dropna(inplace=True)

# Remove duplicate rows
data.drop_duplicates(inplace=True)

# Sort by ticker and date
data.sort_values(["Ticker", "Date"], inplace=True)

# Save cleaned dataset
data.to_csv("data/stocks_2024_clean.csv", index=False)

# Display results
print("CLEANED DATA:")
print(data.head())

print("\nDATA TYPES:")
print(data.dtypes)

print("\nMISSING VALUES:")
print(data.isnull().sum())

print("\nDUPLICATE ROWS:")
print(data.duplicated().sum())

print("\nDATASET SHAPE:")
print(data.shape)

print("\nROWS PER STOCK:")
print(data["Ticker"].value_counts())