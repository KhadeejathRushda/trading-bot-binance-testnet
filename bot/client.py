from binance.client import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Create Binance client
client = Client(
    api_key=API_KEY,
    api_secret=API_SECRET,
    testnet=True
)