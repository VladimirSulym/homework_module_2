import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


def test_filter_by_currency_1(my_lis_transactions):
    generator = filter_by_currency(my_lis_transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    with pytest.raises(StopIteration) as exc_info:
        next(generator)
        assert str(exc_info.value) == "StopIteration"


def test_filter_by_currency_2(my_lis_transactions):
    generator = filter_by_currency(my_lis_transactions, "RUB")
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }
    with pytest.raises(StopIteration) as exc_info:
        next(generator)
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(filter_by_currency(my_lis_transactions, None))
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(filter_by_currency(my_lis_transactions, "EUR"))
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(filter_by_currency([], None))
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(filter_by_currency([], "RUB"))
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(filter_by_currency([], 123))
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(filter_by_currency([]))
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(filter_by_currency())
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(
            filter_by_currency(
                [
                    {
                        "id": 873106923,
                        "state": "EXECUTED",
                        "date": "2019-03-23T01:09:46.296404",
                        "operationAmount": {"amount": "43318.34"},
                        "description": "Перевод со счета на счет",
                        "from": "Счет 44812258784861134719",
                        "to": "Счет 74489636417521191160",
                    }
                ],
                "RUB",
            )
        )
        assert str(exc_info.value) == "StopIteration"


def test_transaction_descriptions_1(my_lis_transactions):
    generator = transaction_descriptions(my_lis_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"

    with pytest.raises(StopIteration) as exc_info:
        next(generator)
        assert str(exc_info.value) == "StopIteration"


def test_transaction_descriptions_2():
    with pytest.raises(StopIteration) as exc_info:
        next(transaction_descriptions([]))
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(transaction_descriptions())
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(transaction_descriptions(None))
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(transaction_descriptions(123))
        assert str(exc_info.value) == "StopIteration"

    with pytest.raises(StopIteration) as exc_info:
        next(
            transaction_descriptions(
                [
                    {
                        "id": 142264268,
                        "state": "EXECUTED",
                        "date": "2019-04-04T23:20:05.206878",
                        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                        "from": "Счет 19708645243227258542",
                        "to": "Счет 75651667383060284188",
                    }
                ]
            )
        )
        assert str(exc_info.value) == "StopIteration"


def test_card_number_generator_1():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"

    with pytest.raises(StopIteration) as exc_info:
        next(generator)
        assert str(exc_info.value) == "StopIteration"


def test_card_number_generator_2():
    generator = card_number_generator(3, 1)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"

    with pytest.raises(StopIteration) as exc_info:
        next(generator)
        assert str(exc_info.value) == "StopIteration"


def test_card_number_generator_3():
    generator = card_number_generator()

    with pytest.raises(StopIteration) as exc_info:
        next(generator)
        assert str(exc_info.value) == "StopIteration"


def test_card_number_generator_4():
    generator = card_number_generator(-10, -8)

    with pytest.raises(StopIteration) as exc_info:
        next(generator)
        assert str(exc_info.value) == "StopIteration"


def test_card_number_generator_5():
    generator = card_number_generator("qweqw", "12")

    with pytest.raises(StopIteration) as exc_info:
        next(generator)
        assert str(exc_info.value) == "StopIteration"
