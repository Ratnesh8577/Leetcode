import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filter big countries (area >= 3,000,000 OR population >= 25,000,000)
    big_countries = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]
    
    # Select required columns
    return big_countries[["name", "population", "area"]]


    