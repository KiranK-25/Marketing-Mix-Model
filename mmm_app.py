from flask import Flask, request, jsonify
import joblib
import json
import numpy as np

# ====================== LOAD MODEL AND FEATURES ======================
model = joblib.load('linear_mmm_model.pkl')

with open('mmm_model_features.json', 'r') as f:
    feature_names = json.load(f)

# ====================== CREATE FLASK APP ======================
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ MMM Model is running! Use /predict endpoint."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        # Prepare features in correct order
        X = [data.get(feat, 0) for feat in feature_names]
        X = np.array(X).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(X)[0]
        
        return jsonify({
            'predicted_revenue': round(float(prediction), 2),
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ====================== RUN THE APP ======================
if __name__ == '__main__':
    print("🚀 Starting Flask MMM API Server...")
    print(f"Expected Features: {feature_names}")
    app.run(debug=True, host='0.0.0.0', port=5000)