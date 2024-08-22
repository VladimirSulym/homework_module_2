from typing import Any


def filter_by_currency(list_transaction: list, currency: str) -> Any:
    for i in list_transaction:
        if i['operationAmount']['currency']['name'] == currency:
            yield i


transactions = [{
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
        "amount": "9824.07",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
}, {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
        "amount": "79114.93",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
}]

usd_transactions = filter_by_currency(transactions, "USD")
for i in range(2):
    try:
        print(next(usd_transactions))
    except StopIteration:
        break
