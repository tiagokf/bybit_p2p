from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from bybit_p2p import P2P
import logging

load_dotenv()

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/connect', methods=['POST'])
def connect_api():
    regions = [
        {"name": "Global", "domain": "bybit", "tld": "com"},
        {"name": "Turkey", "domain": "bybit", "tld": "tr"},
        {"name": "Kazakhstan", "domain": "bybit", "tld": "kz"},
        {"name": "Netherlands", "domain": "bybit", "tld": "nl"}
    ]
    
    for region in regions:
        try:
            logger.info(f"Tentando conectar via {region['name']}")
            api = P2P(
                testnet=False,
                api_key=os.getenv("BYBIT_API_KEY"),
                api_secret=os.getenv("BYBIT_API_SECRET"),
                domain=region["domain"],
                tld=region["tld"]
            )
            # Testa a conexão
            api.get_account_information()
            return jsonify({"success": True, "message": f"Conectado via {region['name']}!"})
        except Exception as e:
            logger.warning(f"Falha em {region['name']}: {str(e)}")
            continue
    
    return jsonify({"success": False, "error": "Não foi possível conectar em nenhuma região"})

@app.route('/api/balance', methods=['GET'])
def get_balance():
    return make_api_call(lambda api: api.get_current_balance(accountType="FUND", coin="USDT"))

@app.route('/api/ads', methods=['GET'])
def get_ads():
    return make_api_call(lambda api: api.get_ads_list())

@app.route('/api/orders', methods=['GET'])
def get_orders():
    return make_api_call(lambda api: api.get_pending_orders())

def make_api_call(func):
    regions = [
        {"domain": "bybit", "tld": "com"},
        {"domain": "bybit", "tld": "tr"},
        {"domain": "bybit", "tld": "kz"},
        {"domain": "bybit", "tld": "nl"}
    ]
    
    for region in regions:
        try:
            api = P2P(
                testnet=False,
                api_key=os.getenv("BYBIT_API_KEY"),
                api_secret=os.getenv("BYBIT_API_SECRET"),
                domain=region["domain"],
                tld=region["tld"]
            )
            result = func(api)
            return jsonify({"success": True, "data": result})
        except Exception as e:
            logger.warning(f"Falha com TLD {region['tld']}: {str(e)}")
            continue
    
    return jsonify({"success": False, "error": "Falha em todas as regiões"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)