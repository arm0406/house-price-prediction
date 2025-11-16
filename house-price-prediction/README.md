# House Price Prediction

A machine learning project for predicting house prices using Linear Regression. This project includes exploratory data analysis, model training, a Flask API for predictions, and Docker support.

## 📋 Project Overview

This project predicts house prices based on various features such as area, number of bedrooms, bathrooms, amenities, and location characteristics. The project includes Jupyter notebook for analysis, multiple model comparisons (Linear Regression, Decision Tree, Random Forest), and a Flask REST API for production predictions.

## 📁 Project Structure

```
house-price-prediction/
├── train.py                    # Model training script (saves trained model)
├── predict.py                  # Flask API server for making predictions
├── serve.py                    # Test script for API (makes sample prediction)
├── api_test.py                 # Alternative API test script
├── notebook.ipynb              # Jupyter notebook with EDA and model exploration
├── dockerfile                  # Docker configuration
├── Pipfile                     # Python dependencies (Pipenv)
├── data/
│   └── Housing.csv            # Dataset with housing features and prices
├── models/
│   └── house_price_model.pkl   # Trained model (generated after running train.py)
└── LICENSE
```

## 🎯 Features

The model predicts prices based on these 12 features:

**Numeric Features:**
- **area**: Total area of the house (in sq ft)
- **bedrooms**: Number of bedrooms
- **bathrooms**: Number of bathrooms
- **stories**: Number of stories
- **parking**: Number of parking spaces

**Binary Features (0/1):**
- **mainroad**: Adjacent to main road
- **guestroom**: Has guest room
- **basement**: Has basement
- **hotwaterheating**: Has hot water heating system
- **airconditioning**: Has air conditioning
- **prefarea**: Located in preferred area

**Categorical Feature:**
- **furnishingstatus**: Furnishing status (encoded)

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- pip or pipenv

### Installation

1. Clone the repository:
```bash
git clone <repository_url>
cd house-price-prediction
```

2. Install dependencies:
```bash
# Using pipenv (recommended)
pipenv install

# Or using pip
pip install pandas numpy seaborn matplotlib scikit-learn joblib flask requests
```

### 1. Train the Model

```bash
python train.py
```

This script will:
- Load the housing dataset from `data/Housing.csv`
- Encode categorical features using LabelEncoder
- Split data into training (80%) and testing (20%) sets
- Train a Linear Regression model
- Save the trained model to `models/house_price_model.pkl`

**Output:**
```
Model trained and saved as models/house_price_model.pkl
```

### 2. Start the API Server

```bash
python predict.py
```

The Flask API will start on `http://0.0.0.0:5000`

### 3. Make Predictions via API

Send a POST request to the `/predict` endpoint:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "area": 7420,
    "bedrooms": 4,
    "bathrooms": 2,
    "stories": 3,
    "mainroad": 1,
    "guestroom": 1,
    "basement": 0,
    "hotwaterheating": 0,
    "airconditioning": 1,
    "parking": 2,
    "prefarea": 1,
    "furnishingstatus": 2
  }'
```

**Response:**
```json
{"predicted_price": 5500000.0}
```

### 4. Test the API

Run the test script (requires the API server to be running):
```bash
python serve.py
```

Or use the alternative test:
```bash
python api_test.py
```

## 📊 Jupyter Notebook Analysis

The `notebook.ipynb` includes:

- **Exploratory Data Analysis (EDA)**: Dataset overview, statistics, and visualizations
- **Feature Analysis**: Value distributions and correlations
- **Model Comparison**: Linear Regression, Decision Tree, and Random Forest models
- **Feature Importance**: Analysis using Random Forest feature importance
- **Performance Metrics**: RMSE comparison across models

To run the notebook:
```bash
jupyter notebook notebook.ipynb
```

## 📦 Dependencies

All dependencies are specified in `Pipfile`:

```toml
pandas          # Data manipulation
numpy           # Numerical computing
scikit-learn    # Machine learning (Linear Regression, DecisionTree, RandomForest)
joblib          # Model serialization
flask           # Web framework for REST API
requests        # HTTP library for testing
matplotlib      # Data visualization
seaborn         # Statistical data visualization
```

Python version: **3.12**

## 🐳 Docker Support

Build and run the project in a Docker container:

```bash
# Build the image
docker build -t house-price-prediction .

# Run the container (exposes port 5000)
docker run -p 5000:5000 house-price-prediction
```

## 📋 API Reference

### POST `/predict`

**Request Body:**
```json
{
  "area": number,
  "bedrooms": number,
  "bathrooms": number,
  "stories": number,
  "mainroad": 0 or 1,
  "guestroom": 0 or 1,
  "basement": 0 or 1,
  "hotwaterheating": 0 or 1,
  "airconditioning": 0 or 1,
  "parking": number,
  "prefarea": 0 or 1,
  "furnishingstatus": number
}
```

**Success Response (200):**
```json
{"predicted_price": 5500000.0}
```

**Error Response (400):**
```json
{"error": "Missing field: area"}
```
or
```json
{"error": "Input contains missing values.", "details": {...}}
```

## 🔄 Workflow

1. **Explore**: Open `notebook.ipynb` for data analysis and model comparison
2. **Train**: Run `python train.py` to train and save the model
3. **Serve**: Run `python predict.py` to start the API server
4. **Predict**: Use `serve.py` or send POST requests to make predictions
5. **Test**: Verify predictions with `api_test.py`

## ⚙️ Technical Details

- **Model**: Linear Regression with encoded categorical features
- **Data Split**: 80% training, 20% testing
- **Input Validation**: Checks for missing fields and null values
- **Binary Feature Handling**: Enforces 0/1 values for binary columns
- **Feature Encoding**: LabelEncoder applied to categorical columns

## 📄 License

See LICENSE file for details.
