import os
from collections import Counter

from config import DATA_PATH
from src.read_csv_xlsx import convert_csv_to_list


def group_agg(dict_list: list, categories_list: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории.
    """
    filter_dict = list(filter(lambda x: x["description"] in categories_list, dict_list))
    data_counting = []
    for i in filter_dict:
        data_counting.append(i["description"])
    counted = Counter(data_counting)
    return dict(counted)

#
# if __name__ == '__main__':
#     # print(
#     #     group_agg(
#     #         convert_csv_to_list(os.path.join(DATA_PATH, "transactions.csv")),
#     #         [
#     #             "Перевод организации",
#     #             "Перевод со счета на счет",
#     #             "Перевод с карты на карту",
#     #             "Открытие вклада",
#     #         ],
#     #     )
#     # )
#
#     print(
#         group_agg(
#             [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
#               'currency_name': 'Sol',
#               'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
#               'description': 'Перевод организации'},
#              {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
#               'currency_name': 'Peso',
#               'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
#               'description': 'Перевод с карты на карту'},
#              {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0,
#               'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
#               'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
#              {'id': 366176.0, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482.0,
#               'currency_name': 'Rupiah',
#               'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420',
#               'description': 'Перевод с карты на карту'},
#              {'id': 5380041.0, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0,
#               'currency_name': 'Peso',
#               'currency_code': 'UYU', 'from': 'nan', 'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'},
#              {'id': 1962667.0, 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': 18588.0,
#               'currency_name': 'Peso',
#               'currency_code': 'COP', 'from': 'Mastercard 7286844946221431', 'to': 'Счет 76145988629288763144',
#               'description': 'Перевод организации'},
#              {'id': 5294458.0, 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': 16836.0,
#               'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198',
#               'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'},
#              {'id': 5429839.0, 'state': 'EXECUTED', 'date': '2023-06-23T19:46:34Z', 'amount': 25261.0,
#               'currency_name': 'Hryvnia', 'currency_code': 'UAH', 'from': 'nan', 'to': 'Счет 76768135089446747029',
#               'description': 'Открытие вклада'},
#              {'id': 3226899.0, 'state': 'EXECUTED', 'date': '2023-04-17T09:21:15Z', 'amount': 21680.0,
#               'currency_name': 'Koruna', 'currency_code': 'CZK', 'from': 'nan', 'to': 'Счет 88329674734590848775',
#               'description': 'Открытие вклада'},
#              {'id': 3176764.0, 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': 16652.0,
#               'currency_name': 'Euro',
#               'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294', 'to': 'American Express 5556525473658852',
#               'description': 'Перевод с карты на карту'},
#              {'id': 4234093.0, 'state': 'EXECUTED', 'date': '2021-07-08T07:31:21Z', 'amount': 23182.0,
#               'currency_name': 'Ruble',
#               'currency_code': 'RUB', 'from': 'Visa 0773092093872450', 'to': 'Discover 8602781449570491',
#               'description': 'Перевод с карты на карту'},
#              {'id': 3107343.0, 'state': 'EXECUTED', 'date': '2023-01-25T13:33:00Z', 'amount': 33639.0,
#               'currency_name': 'Krona',
#               'currency_code': 'SEK', 'from': 'nan', 'to': 'Счет 35662766798195077538', 'description': 'Открытие вклада'},
#              {'id': 2130098.0, 'state': 'PENDING', 'date': '2020-06-07T11:11:36Z', 'amount': 30731.0,
#               'currency_name': 'Euro',
#               'currency_code': 'EUR', 'from': 'Visa 5749750597771353', 'to': 'American Express 9106381490184499',
#               'description': 'Перевод с карты на карту'},
#              {'id': 4653427.0, 'state': 'PENDING', 'date': '2020-10-04T12:12:23Z', 'amount': 34072.0,
#               'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Discover 9058011549803523',
#               'to': 'Mastercard 5266726031439012', 'description': 'Перевод с карты на карту'},
#              {'id': 4641894.0, 'state': 'EXECUTED', 'date': '2021-08-30T12:27:22Z', 'amount': 11111.0,
#               'currency_name': 'Krona',
#               'currency_code': 'SEK', 'from': 'nan', 'to': 'Счет 53688013223998817599', 'description': 'Открытие вклада'}],
#             [
#                 "Перевод организации",
#                 "Перевод со счета на счет",
#                 "Перевод с карты на карту",
#                 "Открытие вклада",
#             ],
#         )
#     )
