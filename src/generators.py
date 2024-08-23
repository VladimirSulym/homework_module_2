from typing import Any


def filter_by_currency(list_transaction: list = None, currency: str = None) -> Any:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции"""
    try:
        if isinstance(list_transaction, list) and isinstance(currency, str):
            for i in list_transaction:
                if i["operationAmount"]["currency"]["code"] == currency:
                    yield i
    except KeyError:
        return


def transaction_descriptions(list_transaction: list = None) -> Any:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    try:
        if isinstance(list_transaction, list):
            for i in list_transaction:
                yield i["description"]
    except KeyError:
        return


def card_number_generator(begin: int, end: int) -> Any:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if end < 10000000000000000:
        for i in range(begin, end + 1):
            temp_number = list(str(10000000000000000 + i))
            del temp_number[0]
            for i in [4, 9, 14]:
                temp_number.insert(i, " ")
            yield "".join(temp_number)


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]
#
# print(next(filter_by_currency([], "USD")))
# usd_transactions = filter_by_currency(transactions, "USD")
# for i in range(5):
#     try:
#         print(next(usd_transactions))
#     except StopIteration:
#         break

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    try:
        print(next(descriptions))
    except StopIteration:
        break
#
# for card_number in card_number_generator(9999888899999990, 9999888899999999):
#     print(card_number)
