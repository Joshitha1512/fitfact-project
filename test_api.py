import requests

url = "https://fitfact-backend.onrender.com/verify_claim"
data = {"claim": "100 sit-ups burn belly fat"}

response = requests.post(url, json=data)
print(response.json())
