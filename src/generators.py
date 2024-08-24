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


def card_number_generator(begin: int = None, end: int = None) -> Any:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if isinstance(begin, int) and isinstance(end, int):
        if end < begin:
            [end, begin] = [begin, end]
        if begin > 0 and 0 < end < 10000000000000000:
            for i in range(begin, end + 1):
                temp_number = list(str(10000000000000000 + i))
                del temp_number[0]
                for i in [4, 9, 14]:
                    temp_number.insert(i, " ")
                yield "".join(temp_number)
