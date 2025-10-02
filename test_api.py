import requests

BASE_URL = "https://fitfact-backend.onrender.com"

def test_home():
    r = requests.get(f"{BASE_URL}/")
    print("Home:", r.status_code, r.text[:100])  

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    print("Health:", r.status_code, r.json())

def test_info():
    r = requests.get(f"{BASE_URL}/info")
    print("Info:", r.status_code, r.json())

def test_verify_claim():
    payload = {"claim": "The Earth orbits the Sun once every 365 days"}
    r = requests.post(f"{BASE_URL}/verify_claim", json=payload)
    print("Verify Claim:", r.status_code, r.json())

if __name__ == "__main__":
    test_home()
    test_health()
    test_info()
    test_verify_claim()
