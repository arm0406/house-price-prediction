# House Price Prediction

## 📋 Project Overview

This project predicts house prices based on various features such as area, number of bedrooms, bathrooms, amenities, and location characteristics. The project includes Jupyter notebook for analysis, multiple model comparisons and a Flask REST API for
predictions.

## 🔍Problem Description
Predicting house prices is a classic regression problem that supports real world decision making for home buyers, sellers, and real estate professionals. The value of a house depends on many factors like area, rooms, amenities, locality, and more—and traditional approaches struggle with complexity and hidden interactions.
This project builds a machine learning model to predict house prices given such features. The solution provides a clean API that, when given new data, instantly outputs a price prediction. The workflow ensures splitting for robust training/validation/testing, tracks all dependencies, and offers a portable, reproducible deployment using Docker.

## 📁 Project Structure

```
house-price-prediction/
├── train.py                    # Model training script (saves trained model).
├── predict.py                  # Flask API server for making predictions.
├── serve.py                    # Test script to test locally.
├── api_test.py                 # Test script for docker.
├── notebook.ipynb              # Jupyter notebook with EDA and model exploration.
├── dockerfile                  # Docker configuration.
├── Pipfile                     # Python dependencies (Pipenv).
├── data/
│   └── Housing.csv            # Dataset with housing features and prices.
├── models/
│   └── house_price_model.pkl   # Trained model (generated after running train.py).
└── LICENSE
```

## 🎯 Features

The model predicts prices based on these 12 features:

**Numeric Features:**
- **area**: Total area of the house
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

### ⬇️Installation

1. Clone the repository:
```bash
git clone https://github.com/arm0406/house-price-prediction.git
cd house-price-prediction
```

2. Install dependencies:

1. All requirements are recorded in pipfile/pipfile.lock.
2. Local setup uses a virtual environment.
3. To install and activate the environment:
```bash
pip install pipenv
pipenv install
pipenv shell
```

3. Train the Model

```bash
python train.py
```
**Output:**
```
Model trained and saved as models/house_price_model.pkl
```

4. Start the Flask API Server

```bash
python predict.py
```

The Flask API will start on `http://0.0.0.0:5000`

 5. Make Predictions via API

Open a new terminal while keeping the API terminal running and send a POST request to the `/predict` endpoint:

```bash
python serve.py
```
## Note: The above process is for running locally and uses port 5000

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

## 🐳 Containerization

1. Application is fully containerized

2. Dockerfile builds everything: dependencies, model, API etc

3. To build and run:
```bash
docker build -t house-price-service .
docker run -p 5050:5000 house-price-service
```

4. This exposes API at `http://localhost:5050/predict` 

## Note: The above process is for running with docker and uses port 5050

## ▶️How to run the project

## A. Locally

1. Activate pipenv shell:
```bash
pipenv shell
```
2. Run the API:
```bash
python predict.py
``` 
3. Make prediction
```bash
python serve.py
```
## B. With Docker

1. Build and run:
```bash
docker build -t house-price-service .
docker run -p 5050:5000 house-price-service
```
2. This exposes API at `http://localhost:5050/predict` 

3. keep the API terminal running and open a new terminal and run:
```bash
python api_test.py
```

## 🔄 Workflow

1. **Explore**: Open `notebook.ipynb` for data analysis and model comparison.
2. **Train**: Run `python train.py` to train and save the model.
3. **Serve**: Run `python predict.py` to start the API server.
4. **Predict**: Use ` python serve.py` to make predictions locally(uses port 5000) and `python api_test.py` to make predictions using docker(uses port 5050).
## NOTE: While running Locally or with Docker make sure that after you run the API whether on port 5000 or 5050, you open a new terminal while keeping the API terminal running.