import requests

# Use localhost if testing locally, or your Render URL if live
BASE_URL = "https://fitfact-backend.onrender.com"

data = {"claim": "100 sit-ups burn belly fat"}

try:
    response = requests.post(f"{BASE_URL}/verify_claim", json=data)
    response.raise_for_status()  # raise error if not 200
    print(response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
