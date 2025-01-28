from bybit_p2p import P2P

api = P2P(
    testnet=True,
    api_key="x",
    api_secret="x"
)

# 1. Get current balance
print(api.get_current_balance(accountType="UNIFIED"))

# 2. Get account information
print(api.get_account_information())

# 3. Get ads list
print(api.get_ads_list())

# 4. Get ad detail
print(api.get_ad_detail())
