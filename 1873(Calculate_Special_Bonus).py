import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id'] % 2 == 1 and not x['name'].startswith('M') else 0, axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')


'''
import numpy as np

employees['bonus'] = np.where(
    (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M')),
    employees['salary'],
    0
)

return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
'''
    