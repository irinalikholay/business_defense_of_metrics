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

## DISTRIBUTION REALITY CHECK

print("\n*** DISTRIBUTION REALITY CHECK *** ")

median_order_value = df["order_value"].median()

p50 = df["order_value"].quantile(0.50)
p75 = df["order_value"].quantile(0.75)
p95 = df["order_value"].quantile(0.95)

print(f"Median order value: {median_order_value:.2f}")
print(f"50th percentile (P50): {p50:.2f}")
print(f"75th percentile (P75): {p75:.2f}")
print(f"95th percentile (P95): {p95:.2f}")

## WHO BREAKS THE METRICS 

print("\n*** WHO BREAKS THE METRICS ***")

df_sorted = df.sort_values(by="order_value", ascending=False)

total_orders = len(df_sorted)
total_revenue = df_sorted["order_value"].sum()

def top_share(df, top_percent):
    top_n = int(len(df) * top_percent)
    top_df = df.head(top_n)

    orders_share = top_n / total_orders * 100
    revenue_share = top_df["order_value"].sum() / total_revenue * 100

    return orders_share, revenue_share

for p in [0.01, 0.05, 0.10]:
    orders_pct, revenue_pct = top_share(df_sorted, p)
    print(
        f"Top {int(p*100)}% orders - "
        f"{orders_pct:.1f}% of orders, "
        f"{revenue_pct:.1f}% of revenue"
    )