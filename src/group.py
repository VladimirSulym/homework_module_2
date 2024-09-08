import os
from collections import Counter

from config import DATA_PATH
from src.read_csv_xlsx import convert_csv_to_list


def group_agg(dict_list: list, categories_list: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    filter_dict = list(filter(lambda x: x["description"] in categories_list, dict_list))
    data_counting = []
    for i in filter_dict:
        data_counting.append(i["description"])
    counted = Counter(data_counting)
    return dict(counted)


# if __name__ == '__main__':
#     print(
#         group_agg(
#             convert_csv_to_list(os.path.join(DATA_PATH, "transactions.csv")),
#             [
#                 "Перевод организации",
#                 "Перевод со счета на счет",
#                 "Перевод с карты на карту",
#                 "Открытие вклада",
#             ],
#         )
#     )
