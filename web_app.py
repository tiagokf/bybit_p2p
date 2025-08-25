from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from bybit_p2p import P2P

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/connect', methods=['POST'])
def connect_api():
    try:
        api = P2P(
            testnet=False,
            api_key=os.getenv("BYBIT_API_KEY"),
            api_secret=os.getenv("BYBIT_API_SECRET")
        )
        return jsonify({"success": True, "message": "Conectado com sucesso!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/balance', methods=['GET'])
def get_balance():
    try:
        api = P2P(
            testnet=False,
            api_key=os.getenv("BYBIT_API_KEY"),
            api_secret=os.getenv("BYBIT_API_SECRET")
        )
        balance = api.get_current_balance(accountType="FUND", coin="USDT")
        return jsonify({"success": True, "data": balance})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/ads', methods=['GET'])
def get_ads():
    try:
        api = P2P(
            testnet=False,
            api_key=os.getenv("BYBIT_API_KEY"),
            api_secret=os.getenv("BYBIT_API_SECRET")
        )
        ads = api.get_ads_list()
        return jsonify({"success": True, "data": ads})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        api = P2P(
            testnet=False,
            api_key=os.getenv("BYBIT_API_KEY"),
            api_secret=os.getenv("BYBIT_API_SECRET")
        )
        orders = api.get_pending_orders()
        return jsonify({"success": True, "data": orders})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)