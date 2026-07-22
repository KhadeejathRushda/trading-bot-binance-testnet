from bot.client import client

try:
    account = client.futures_account()
    print("✅ Connected successfully!")
except Exception as e:
    print("❌ Connection failed!")
    print(e)