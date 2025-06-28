
import requests
import os

GOLD_API_KEY = os.getenv("GOLD_API_KEY", "your_real_goldapi_key_here")

def get_live_gold_price():
    url = f"https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()
