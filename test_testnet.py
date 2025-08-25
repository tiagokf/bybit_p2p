from dotenv import load_dotenv
import os
from bybit_p2p import P2P

load_dotenv()

print("=== Testando Testnet ===")

try:
    # Tenta testnet primeiro
    api = P2P(
        testnet=True,
        api_key=os.getenv("BYBIT_API_KEY"),
        api_secret=os.getenv("BYBIT_API_SECRET")
    )
    
    result = api.get_account_information()
    print("✅ SUCESSO no Testnet")
    print(result)
    
except Exception as e:
    error_msg = str(e)
    print(f"❌ ERRO no Testnet: {error_msg}")
    
    if "10003" in error_msg:
        print("   → Suas credenciais são apenas para produção")
    elif "403" in error_msg:
        print("   → IP bloqueado também no testnet")

print("\n=== Verificando se precisa de credenciais testnet ===")
print("Se erro 10003: suas credenciais são só para produção")
print("Se erro 403: problema de IP/região")