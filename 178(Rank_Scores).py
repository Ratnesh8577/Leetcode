import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    
    # Return only score and rank, ordered by score descending
    result = scores[['score', 'rank']].sort_values(by='score', ascending=False).reset_index(drop=True)
    
    return result
    