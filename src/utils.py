import json
import os.path

from config import DATA_PATH
from src.external_api import currency_conversion


def get_data_json(my_path):
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(my_path, "r") as f:
            return json.load(f)
    except Exception:
        return []


base_data = get_data_json(os.path.join(DATA_PATH, "operations.json"))


def get_amount_transactions_in_rub(transaction):
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            return currency_conversion(
                transaction["operationAmount"]["currency"]["code"], transaction["operationAmount"]["amount"]
            )
        else:
            return float(transaction["operationAmount"]["amount"])
    except Exception:
        return None


#
# for i in range(0, 5):
#     print(get_amount_transactions_in_rub(base_data[i]))
