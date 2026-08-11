import pandas as pd

# Load raw data
data = pd.read_csv("data/aapl_2024_raw.csv")

# Remove the two extra header rows
data = data.iloc[2:].copy()

# Rename the first column
data.rename(columns={"Price": "Date"}, inplace=True)

# Convert columns to the correct data types
data["Date"] = pd.to_datetime(data["Date"])

numeric_columns = ["Close", "High", "Low", "Open", "Volume"]

for column in numeric_columns:
    data[column] = pd.to_numeric(data[column], errors="coerce")

# Check the cleaned data
print("CLEANED DATA:")
print(data.head())

print("\nDATA TYPES:")
print(data.dtypes)

print("\nMISSING VALUES:")
print(data.isnull().sum())

print("\nROWS AND COLUMNS:")
print(data.shape)

# Save cleaned data
data.to_csv("data/aapl_2024_clean.csv", index=False)

print("\nCleaned data saved successfully!")