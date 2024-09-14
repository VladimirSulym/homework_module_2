from src.search import transaction_search


def test_transaction_search(my_list_dict_long):
    assert transaction_search(my_list_dict_long, 'Euro') == [
        {'id': 3176764.0, 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': 16652.0,
         'currency_name': 'Euro',
         'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294',
         'to': 'American Express 5556525473658852',
         'description': 'Перевод с карты на карту'},
        {'id': 2130098.0, 'state': 'PENDING', 'date': '2020-06-07T11:11:36Z', 'amount': 30731.0,
         'currency_name': 'Euro',
         'currency_code': 'EUR', 'from': 'Visa 5749750597771353',
         'to': 'American Express 9106381490184499',
         'description': 'Перевод с карты на карту'}
    ]

    assert transaction_search(my_list_dict_long, 'Visa') == [
        {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0,
         'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
         'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
    ]

    assert transaction_search([], 'Euro') == []
    assert transaction_search(my_list_dict_long, '') == my_list_dict_long
    assert transaction_search(my_list_dict_long, None) == my_list_dict_long
    assert transaction_search(None, None) == []