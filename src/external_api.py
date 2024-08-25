import os

import requests
from dotenv import load_dotenv

load_dotenv()


def currency_conversion(currency, amount):
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "to": "RUB",
        "from": currency,
        "amount": str(amount),
    }
    headers = {"apikey": os.getenv("API_KEY")}
    response = requests.get(url, headers=headers, params=payload)
    # status_code = response.status_code
    result = response.json()
    return round(result["result"], 2)
