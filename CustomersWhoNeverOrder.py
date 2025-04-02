import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers['id'].isin(orders['customerId'])][['name']]
    return result.rename(columns={'name': 'Customers'})
    


'''
# Example usage
customers_data = {'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max']}
customers = pd.DataFrame(customers_data)

orders_data = {'id': [1, 2], 'customerId': [3, 1]}
orders = pd.DataFrame(orders_data)

print(customers_without_orders(customers, orders))
'''
