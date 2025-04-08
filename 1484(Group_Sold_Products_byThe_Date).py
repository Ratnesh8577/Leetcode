import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    result = (
        activities
        .groupby('sell_date')['product']                      # Group by sell_date
        .apply(lambda x: ','.join(sorted(set(x))))           # Sort and join unique product names
        .reset_index(name='products')                         # Reset index and name column
    )
    
    # Count number of products sold per day
    result['num_sold'] = result['products'].apply(lambda x: len(x.split(',')))
    
    # Reorder columns
    result = result[['sell_date', 'num_sold', 'products']]
    
    # Sort by sell_date
    result = result.sort_values(by='sell_date').reset_index(drop=True)
    
    return result
    