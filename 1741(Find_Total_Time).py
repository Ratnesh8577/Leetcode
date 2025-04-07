import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    
    # Step 2: Group by emp_id and event_day and sum the time
    result = employees.groupby(['event_day', 'emp_id'], as_index=False)['time_spent'].sum()
    
    # Step 3: Rename columns to match expected output
    result.rename(columns={'event_day': 'day', 'time_spent': 'total_time'}, inplace=True)
    
    return result
    