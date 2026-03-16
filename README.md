# Customer Lifetime Value Prediction

Predicts future customer spending using Random Forest Regression on RFM features.

## Project Structure
- `src/`: Data generation and training logic.
- `models/`: Learned regression model.
- `app.py`: Real-time Streamlit interface.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train the model (uses synthetic data):
   ```bash
   python src/train.py
   ```

## Usage
Run the web application:
```bash
streamlit run app.py
```
Enter Recency, Frequency, and Monetary values to estimate future value.
