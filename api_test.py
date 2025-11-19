import requests

data = {
    "area": 7777,
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
}

response = requests.post("http://localhost:5050/predict", json=data)
print(response.json())