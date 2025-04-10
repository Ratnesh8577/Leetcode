import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Count number of direct reports for each managerId
    report_counts = employee.groupby('managerId').size().reset_index(name='report_count')
    
    # Filter for managers with 5 or more reports
    managers_with_5 = report_counts[report_counts['report_count'] >= 5]
    
    # Merge with employee table to get manager names
    result = pd.merge(managers_with_5, employee, left_on='managerId', right_on='id')[['name']]
    
    return result
