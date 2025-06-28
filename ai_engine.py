from datetime import datetime

def generate_trade_signal():
    return {
        "entry": "Waiting for signal...",
        "stop_loss": "Calculating...",
        "take_profit": "Calculating...",
        "confidence": "0.0%",
        "status": "WAIT",
        "timestamp": datetime.utcnow().isoformat()
    }