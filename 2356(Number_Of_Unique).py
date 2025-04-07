import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    unique_subjects = teacher[['teacher_id', 'subject_id']].drop_duplicates()
    
    # Group by teacher_id and count unique subjects
    result = unique_subjects.groupby('teacher_id').size().reset_index(name='cnt')
    
    return result
    