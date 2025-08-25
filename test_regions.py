from dotenv import load_dotenv
import os
from bybit_p2p import P2P

load_dotenv()

# Testa diferentes domínios/regiões
regions = [
    {"name": "Global", "domain": "bybit.com", "tld": "com"},
    {"name": "Turkey", "domain": "bybit.com", "tld": "tr"},
    {"name": "Kazakhstan", "domain": "bybit.com", "tld": "kz"},
    {"name": "Netherlands", "domain": "bybit.com", "tld": "nl"},
]

for region in regions:
    try:
        print(f"\n=== Testando {region['name']} ===")
        
        api = P2P(
            testnet=False,
            api_key=os.getenv("BYBIT_API_KEY"),
            api_secret=os.getenv("BYBIT_API_SECRET"),
            domain=region["domain"],
            tld=region["tld"]
        )
        
        result = api.get_account_information()
        print(f"✅ SUCESSO em {region['name']}")
        print(result)
        break
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ ERRO em {region['name']}: {error_msg}")
        
        if "403" in error_msg:
            print("   → IP bloqueado nesta região")
        elif "10010" in error_msg:
            print("   → IP não autorizado na API key")
        elif "10003" in error_msg:
            print("   → Credenciais inválidas")

print("\n=== Teste concluído ===")