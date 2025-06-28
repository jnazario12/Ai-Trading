from flask import Flask, jsonify
from gold_api import get_gold_price
from ai_engine import generate_trade_signal

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ APEX PARAGON AI is running live!"

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "running", "ai": "APEX PARAGON AI v2.2.1"})

@app.route("/price", methods=["GET"])
def price():
    return jsonify(get_gold_price())

@app.route("/trade", methods=["GET"])
def trade():
    return jsonify(generate_trade_signal())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)