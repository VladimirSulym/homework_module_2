from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


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
        assert str(exc_info.value) == 'StopIteration'


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
        assert str(exc_info.value) == 'StopIteration'

# @pytest.mark.parametrize('lis_transactions, currency, expected', [
#     ([{
#          "id": 939719570,
#          "state": "EXECUTED",
#          "date": "2018-06-30T02:08:58.425572",
#          "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#          "description": "Перевод организации",
#          "from": "Счет 75106830613657916952",
#          "to": "Счет 11776614605963066702",
#      }], "USD", {
#          "id": 939719570,
#          "state": "EXECUTED",
#          "date": "2018-06-30T02:08:58.425572",
#          "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#          "description": "Перевод организации",
#          "from": "Счет 75106830613657916952",
#          "to": "Счет 11776614605963066702",
#      }),
# ([{
#          "id": 939719570,
#          "state": "EXECUTED",
#          "date": "2018-06-30T02:08:58.425572",
#          "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#          "description": "Перевод организации",
#          "from": "Счет 75106830613657916952",
#          "to": "Счет 11776614605963066702",
#      }], "RUB", )
# ])
# def test_filter_by_currency_2(lis_transactions, currency, expected):
#     generator = filter_by_currency(lis_transactions, currency)
#     assert next(generator) == expected
