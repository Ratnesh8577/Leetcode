import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_company_ids = company[company['name'] == 'RED']['com_id']

    # Step 2: Get salespersons who had orders with 'RED' company
    sales_with_red_orders = orders[orders['com_id'].isin(red_company_ids)]['sales_id'].unique()

    # Step 3: Filter out those salespersons from the full sales_person table
    result = sales_person[~sales_person['sales_id'].isin(sales_with_red_orders)][['name']]

    return result
    