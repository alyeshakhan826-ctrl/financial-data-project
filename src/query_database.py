import sqlite3

# Connect to the database
connection = sqlite3.connect("financial_data.db")

# SQL query
query = """
SELECT
    Ticker,

    MAX(CASE
        WHEN Date = '2024-01-02' THEN Close
    END) AS Start_Price,

    MAX(CASE
        WHEN Date = '2024-12-31' THEN Close
    END) AS End_Price

FROM stock_prices
GROUP BY Ticker;
"""

# Run query
results = connection.execute(query)

print("2024 STOCK RETURNS:")

for row in results:
    ticker = row[0]
    start_price = row[1]
    end_price = row[2]

    total_return = ((end_price - start_price) / start_price) * 100

    print(
        f"{ticker}: "
        f"${start_price:.2f} → ${end_price:.2f} | "
        f"Return: {total_return:.2f}%"
    )

# Close database
connection.close()