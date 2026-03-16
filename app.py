import streamlit as st
import pandas as pd
import joblib
import os
import plotly.graph_objects as go

st.set_page_config(page_title="CLV Predictor", layout="centered")

MODEL_PATH = "models/clv_model.pkl"

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

st.title("💰 Customer Lifetime Value Prediction")
st.write("Predict the future 3-month spending of a customer based on RFM metrics.")

model = load_model()

if model is None:
    st.error("Model not found. Please run `src/train.py` first.")
else:
    with st.form("input_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            recency = st.number_input("Recency (Days)", min_value=0, value=30, help="Days since last purchase")
        with col2:
            frequency = st.number_input("Frequency", min_value=1, value=5, help="Total number of orders")
        with col3:
            monetary = st.number_input("Monetary ($)", min_value=0.0, value=500.0, help="Total amount spent")
            
        submit = st.form_submit_button("Predict CLV")
        
    if submit:
        # Create input dataframe
        input_data = pd.DataFrame([{
            'Recency': recency,
            'Frequency': frequency,
            'Monetary': monetary
        }])
        
        prediction = model.predict(input_data)[0]
        
        st.subheader(f"Predicted Spend (Next 3 Months):")
        st.success(f"$ {prediction:.2f}")
        
        # Visualize relative to inputs
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = prediction,
            title = {'text': "CLV Score"},
            gauge = {'axis': {'range': [0, max(1000, prediction*1.5)]},
                     'bar': {'color': "#2E8B57"}}
        ))
        st.plotly_chart(fig)
