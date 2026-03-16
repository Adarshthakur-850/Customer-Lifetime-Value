import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_transactions(n_customers=1000, n_transactions=5000):
    np.random.seed(42)
    random.seed(42)
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_range = (end_date - start_date).days
    
    data = []
    
    for _ in range(n_transactions):
        customer_id = random.randint(1, n_customers)
        days_offset = random.randint(0, date_range)
        order_date = start_date + timedelta(days=days_offset)
        
        # Amount: Gamma distribution (skewed towards lower values, some high spenders)
        amount = np.random.gamma(shape=2.0, scale=30.0) 
        amount = round(max(5.0, amount), 2)
        
        data.append({
            'customer_id': customer_id,
            'order_date': order_date,
            'amount': amount
        })
        
    df = pd.DataFrame(data)
    df.sort_values('order_date', inplace=True)
    return df

if __name__ == "__main__":
    df = generate_transactions()
    print(df.head())
    print(f"Total Sales: {df['amount'].sum()}")
