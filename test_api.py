import requests

url = "http://127.0.0.1:5000/verify_claim"
data = {"claim": "100 sit-ups burn belly fat"}

response = requests.post(url, json=data)
print(response.json())
