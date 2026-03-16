import pandas as pd
from datetime import datetime

def calculate_rfm(transactions, analysis_date):
    """
    Calculates Recency, Frequency, Monetary value up to analysis_date.
    """
    # Filter past transactions
    history = transactions[transactions['order_date'] <= analysis_date].copy()
    
    rfm = history.groupby('customer_id').agg({
        'order_date': lambda x: (analysis_date - x.max()).days,
        'customer_id': 'count',
        'amount': 'sum'
    }).rename(columns={
        'order_date': 'Recency',
        'customer_id': 'Frequency',
        'amount': 'Monetary'
    })
    
    return rfm

def create_features_and_target(transactions):
    """
    Splits data into calibration (features) and observation (target) periods.
    Calibration: Jan 1 - Sept 30
    Observation: Oct 1 - Dec 31
    """
    cutoff_date = datetime(2023, 9, 30)
    
    # Features (X)
    X = calculate_rfm(transactions, cutoff_date)
    
    # Target (y): Spend after cutoff
    future = transactions[transactions['order_date'] > cutoff_date]
    y = future.groupby('customer_id')['amount'].sum().rename('CLV_3_Months')
    
    # Merge X and y (fill missing targets with 0 - they churned or didn't buy)
    dataset = X.join(y, how='left').fillna(0)
    
    return dataset
