import os
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()


def currency_conversion(currency: str, amount: str) -> Optional[float]:
    """Функция конвертации валют по внешнему API"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "to": "RUB",
        "from": currency,
        "amount": str(amount),
    }
    headers = {"apikey": os.getenv("API_KEY")}
    response = requests.get(url, headers=headers, params=payload)
    result = response.json()
    return round(result["result"], 2)


# def currency_symbols_base():
#     url = "https://api.apilayer.com/exchangerates_data/symbols"
#     headers = {"apikey": os.getenv("API_KEY")}
#     response = requests.get(url, headers=headers)
#     return list(response.json()['symbols'].keys())
#
# symbols_base = currency_symbols_base()
#
# def currency_conversion(currency: str, amount: str) -> Optional [float]:
#     url = "https://api.apilayer.com/exchangerates_data/convert"
#     if (currency.upper() in symbols_base) and str(amount).isdigit():
#         payload = {
#             "to": "RUB",
#             "from": currency,
#             "amount": str(amount),
#         }
#         headers = {"apikey": os.getenv("API_KEY")}
#         response = requests.get(url, headers=headers, params=payload)
#         result = response.json()
#         return round(result["result"], 2)
#     else:
#         return None
