import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=('lead_id', pd.Series.nunique),
        unique_partners=('partner_id', pd.Series.nunique)
    ).reset_index()
    
    return result
    