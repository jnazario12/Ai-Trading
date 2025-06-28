
from fastapi import FastAPI
from gold_api import get_live_gold_price

app = FastAPI()

@app.get("/")
def root():
    return {"message": "APEX PARAGON AI v2.2.0 is live"}

@app.get("/price")
def get_price():
    return get_live_gold_price()
