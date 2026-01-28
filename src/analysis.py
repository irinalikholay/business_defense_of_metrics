import pandas as pd
from pathlib import Path

## NAIVE METRIC ANALYSIS

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "orders_raw.csv"

df = pd.read_csv(RAW_DATA_PATH)

df["order_date"] = pd.to_datetime(df["order_date"])

total_orders = len(df)
total_revenue = df["order_value"].sum()
average_order_value = df["order_value"].mean()

print("\n*** NAIVE BUSINESS METRICS ***")
print(f"Total orders: {total_orders}")
print(f"Total revenue: {total_revenue:.2f}")
print(f"Average Order Value (AOV): {average_order_value:.2f}")