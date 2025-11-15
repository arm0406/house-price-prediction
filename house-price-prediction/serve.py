import requests

data = {
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
}

response = requests.post("http://127.0.0.1:5000/predict", json=data)
print(response.json())