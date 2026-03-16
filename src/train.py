import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_loader import generate_transactions
from src.preprocessing import create_features_and_target

def train():
    print("Generating data...")
    df = generate_transactions(n_customers=2000, n_transactions=10000)
    
    print("Creating features (RFM) and targets...")
    data = create_features_and_target(df)
    
    X = data[['Recency', 'Frequency', 'Monetary']]
    y = data['CLV_3_Months']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest Regressor...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluation
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    
    print(f"Model Performance:")
    print(f"MAE: ${mae:.2f}")
    print(f"R2 Score: {r2:.3f}")
    
    # Save Model
    if not os.path.exists("models"):
        os.makedirs("models")
    joblib.dump(model, "models/clv_model.pkl")
    print("Model saved to models/clv_model.pkl")
    
    # Feature Importance Plot
    if not os.path.exists("plots"):
        os.makedirs("plots")
        
    imp = pd.Series(model.feature_importances_, index=X.columns)
    plt.figure(figsize=(6,4))
    imp.sort_values().plot(kind='barh', color='teal')
    plt.title("Feature Importance")
    plt.savefig("plots/feature_importance.png")
    plt.close()

if __name__ == "__main__":
    train()
