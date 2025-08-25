from dotenv import load_dotenv
import os
from bybit_p2p import P2P

load_dotenv()

print("=== Teste Simples - Apenas Global ===")

try:
    api = P2P(
        testnet=False,
        api_key=os.getenv("BYBIT_API_KEY"),
        api_secret=os.getenv("BYBIT_API_SECRET")
    )
    
    print("✅ API criada com sucesso")
    print("Tentando obter informações da conta...")
    
    result = api.get_account_information()
    print("✅ SUCESSO!")
    print(result)
    
except Exception as e:
    error_msg = str(e)
    print(f"❌ ERRO: {error_msg}")
    
    if "403" in error_msg:
        print("\n🚫 PROBLEMA: IP bloqueado geograficamente")
        print("💡 SOLUÇÕES:")
        print("1. Usar VPN para mudar localização")
        print("2. Configurar IP whitelist na API key")
        print("3. Criar nova API key sem restrições")
    elif "10010" in error_msg:
        print("\n🚫 PROBLEMA: IP não autorizado na API key")
    elif "10003" in error_msg:
        print("\n🚫 PROBLEMA: Credenciais inválidas")