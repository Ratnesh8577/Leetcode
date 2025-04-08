import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    melted = products.melt(id_vars="product_id", 
                           value_vars=["store1", "store2", "store3"],
                           var_name="store",
                           value_name="price")
    
    # Drop rows with null prices
    result = melted.dropna(subset=["price"])
    
    return result
    