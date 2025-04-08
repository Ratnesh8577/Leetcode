import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return (
        orders
        .groupby('customer_number')         # Group by customer
        .size()                             # Count number of orders
        .reset_index(name='order_count')    # Reset index to get a proper DataFrame
        .sort_values(by='order_count', ascending=False)  # Sort by count descending
        .head(1)[['customer_number']]       # Get the top customer
    )
    