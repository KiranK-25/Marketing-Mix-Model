# 📊 Marketing Mix Modeling (MMM) for Marketing Budget Optimization

A complete **Marketing Mix Modeling (MMM)** project that predicts revenue based on marketing spend across multiple channels. Includes model training, Flask API, and a clean web interface.

---

## 🚀 Features

- Trained Linear Regression Model
- Revenue Prediction API using Flask
- Interactive Web Interface (`index.html`)
- Feature engineering and ROI analysis in Jupyter Notebook
- Easy to test "What-If" marketing budget scenarios

---

## 📁 Project Structure

- `ecommerce_mmm_model_training.ipynb` → Model training notebook
- `mmm_app.py` → Flask Backend API
- `index.html` → Web User Interface
- `linear_mmm_model.pkl` → Trained Model
- `mmm_model_features.json` → Features used by model
- `compressed_data.csv.gz` → Dataset (compressed)

---

## 🛠️ How to Run Locally

1. Install dependencies:
   ```bash
   pip install flask flask-cors joblib numpy scikit-learn pandas
