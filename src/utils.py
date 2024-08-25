import os.path
import json
from config import DATA_PATH
from src.external_api import currency_conversion

def get_data_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

base_data = get_data_json(os.path.join(DATA_PATH, 'operations.json'))

def get_amount_transactions_in_rub(transaction):
    if transaction['operationAmount']['currency']['code'] != 'RUB':
        return currency_conversion(transaction['operationAmount']['currency']['code'],
                            transaction['operationAmount']['amount'])
    else:
        return transaction['operationAmount']['amount']

for i in range(10, 15):
    print(get_amount_transactions_in_rub(base_data[i]))