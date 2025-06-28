import requests

API_KEY = "YOUR_REAL_GOLDAPI_KEY"
API_URL = "https://www.goldapi.io/api/XAU/USD"

def get_gold_price():
    headers = {"x-access-token": API_KEY, "Content-Type": "application/json"}
    try:
        res = requests.get(API_URL, headers=headers)
        if res.status_code == 200:
            data = res.json()
            return {"price": data.get("price", 0), "source": "GoldAPI", "success": True}
        else:
            return {"error": "Failed to fetch price", "status": res.status_code, "success": False}
    except Exception as e:
        return {"error": str(e), "success": False}