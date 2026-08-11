import sqlite3
import pandas as pd

# Load cleaned stock data
data = pd.read_csv("data/stocks_2024_clean.csv")

# Connect to SQLite database
connection = sqlite3.connect("financial_data.db")

# Load data into SQL
data.to_sql(
    "stock_prices",
    connection,
    if_exists="replace",
    index=False
)

print("Five-stock data successfully loaded into SQLite!")

# Check number of rows
result = connection.execute(
    "SELECT COUNT(*) FROM stock_prices;"
)

row_count = result.fetchone()[0]

print(f"Rows in database: {row_count}")

# Close connection
connection.close()