import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Get unique salaries in descending order
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)

    # Get the Nth highest salary or None if it doesn't exist
    if N <= len(unique_salaries):
        nth_salary = unique_salaries.iloc[N - 1]  # use iloc instead of []
    else:
        nth_salary = None

    # Return result in expected LeetCode format
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})
    