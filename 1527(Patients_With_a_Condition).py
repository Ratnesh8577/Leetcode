import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    filtered_patients = patients[
        patients["conditions"].apply(lambda x: any(word.startswith("DIAB1") for word in str(x).split()))
    ]
    
    return filtered_patients