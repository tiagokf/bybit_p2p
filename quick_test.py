from dotenv import load_dotenv
import os
from bybit_p2p import P2P

# Carrega credenciais do .env
load_dotenv()

# Tente primeiro com testnet=False (produção)
api = P2P(
    testnet=False,  # Mudando para produção
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_API_SECRET")
)

# Teste rápido
try:
    print("=== Informacoes da Conta ===")
    account_info = api.get_account_information()
    print(account_info)
    
    print("\n=== Saldo ===")
    balance = api.get_current_balance(accountType="FUND", coin="USDT")
    print(balance)
    
except Exception as e:
    print(f"Erro: {str(e)}")