import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Loading the trained model
model = joblib.load('models/house_price_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    x_new = pd.DataFrame([data])
    # Ensuring all the columns are present
    expected = [
        "area", "bedrooms", "bathrooms", "stories", "mainroad", "guestroom",
        "basement", "hotwaterheating", "airconditioning", "parking", "prefarea", "furnishingstatus"
    ]
    for col in expected:
        if col not in x_new.columns:
            return jsonify({'error': f"Missing field: {col}"})
    
    # Manually enforcing binary i.e 0 & 1for binary columns
    binary_cols = [
        "mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea"
    ]
    for col in binary_cols:
        x_new[col] = x_new[col].apply(lambda v: 1 if v == 1 else 0)

    # Check for any missing values
    if x_new.isnull().any().any():
        return jsonify({'error': 'Input contains missing values.', 'details': x_new.isnull().sum().to_dict()})

    prediction = model.predict(x_new)[0]
    return jsonify({'predicted_price': prediction})

if __name__ == '__main__':
    app.run(debug=True)
