# Customer Lifetime Value Prediction

This repository implements a **Customer Lifetime Value (CLV)** prediction solution using machine learning.  
CLV is a key metric used in business analytics to estimate the **future monetary value** a customer brings over time, enabling better marketing spend, retention strategy, and business growth planning. :contentReference[oaicite:1]{index=1}

---

## 📌 Overview

Customer Lifetime Value quantifies the expected **total spending** a customer will make throughout their relationship with a business.  
This project trains a regression model using **Recency, Frequency, and Monetary (RFM)** features and provides a real-time interface to predict CLV for new input values.

---

## 🚀 Features

- **Data Generation & Preprocessing** – Structured data pipeline for training models
- **ML Model (Random Forest Regression)** – Predicts CLV based on key behavioral features
- **Interactive Web Interface** – Streamlit app for testing predictions live
- **Modular Project Structure** – Easy to extend/add models

---

## 📂 Project Structure

```

├── models/                # Saved machine learning models
├── plots/                 # Visualizations and EDA outputs
├── src/                   # Source logic (data, training, utils)
│   └── train.py           # Model training script
├── app.py                 # Streamlit application entrypoint
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── Screenshot 2026-02-05 001002.png # Example UI screenshot

````

---

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Adarshthakur-850/Customer-Lifetime-Value.git
cd Customer-Lifetime-Value
````

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Train the model**

*(This trains the CLV regression model on your dataset)*

```bash
python src/train.py
```

5. **Launch the web app**

```bash
streamlit run app.py
```

---

## 📈 Usage

Once the Streamlit app launches, you can:

* Enter **Recency**, **Frequency**, and **Monetary** inputs
* Instantly receive a **predicted Customer Lifetime Value**
* Use the output to support decisions such as targeted marketing or budgeting

---

## 📊 Example Output

> *(Replace below screenshot with your actual UI example)*

![App UI](Screenshot%202026-02-05%20001002.png)

---

## 🔍 How It Works

1. **Feature Extraction** – RFM values are collected or generated
2. **Model Training** – Random Forest Regressor learns the relationship between RFM and lifetime value
3. **Prediction Interface** – A lightweight Streamlit interface makes predictions in real time

CLV prediction is a critical business metric that allows firms to understand customer value over time and align marketing and retention strategies for better ROI. ([Wikipedia][1])

---

## 📦 Dependencies

All required packages are listed in `requirements.txt`. Typical dependencies include:

* streamlit
* scikit-learn
* pandas
* numpy

---

## 📝 Notes

* Ensure you have a compatible Python version (3.7+ recommended)
* You can replace or extend the model (e.g., XGBoost, LightGBM) for improved performance
* Integrate actual customer datasets instead of synthetic data for production usage

---

## 📌 Future Improvements

* Add **cross-validation and hyperparameter tuning**
* Deploy the app via **Streamlit Cloud** or **Heroku**
* Add **customer segmentation** (e.g., gold/silver/bronze tiers)
* Add **model evaluation dashboards**

---

## 📜 License

This project is under the **MIT License** — free to use and modify.

---

## 📫 Contact

For questions or collaboration, connect with me via GitHub!

---

Let me know if you want this formatted with badges, deployment links, or automated CI (GitHub Actions) steps!

[1]: https://en.wikipedia.org/wiki/Customer_lifetime_value?utm_source=chatgpt.com "Customer lifetime value"
