import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filter_Product= products[(products["low_fats"]=="Y" ) & (products["recyclable"]=="Y")]


    return filter_Product[["product_id"]]
    