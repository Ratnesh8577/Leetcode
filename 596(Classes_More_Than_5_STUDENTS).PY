import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses.groupby("class").size().reset_index(name="student_count")
    
    # Filter classes with at least 5 students
    result = class_counts[class_counts["student_count"] >= 5][["class"]]
    
    return result
    