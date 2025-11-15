import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Loading dataset
df = pd.read_csv('data/Housing.csv')  # Change file name as needed

# Encoding categorical features same way as in the notebook:
categorical_cols = [
    'mainroad', 'guestroom', 'basement', 'hotwaterheating',
    'airconditioning', 'prefarea', 'furnishingstatus'
]
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Splitting the features and the target
X = df.drop('price', axis=1)
y = df['price']

# Train,test & split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Saving the model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/house_price_model.pkl')
print("Model trained and saved as models/house_price_model.pkl")