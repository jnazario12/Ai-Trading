import requests

def get_live_gold_price(api_key):
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()
