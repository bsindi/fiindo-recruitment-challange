import requests

BASE_URL = "https://api.test.fiindo.com/api/v1"
HEADERS = {"Authorization": "Bearer barzan.sindi"}

def get_tickers():
    """Fetch all tickers from the Fiindo API."""
    response = requests.get(f"{BASE_URL}/tickers", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_ticker_details(symbol: str):
    """Fetch detailed data for a specific ticker."""
    response = requests.get(f"{BASE_URL}/tickers/{symbol}", headers=HEADERS)
    response.raise_for_status()
    return response.json()
