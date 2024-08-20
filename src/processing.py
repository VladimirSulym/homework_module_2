"""Модул содержит 2 функции работы о словарями"""

from typing import Iterable, Union


def filter_by_state(my_list: Union[list], state: Union[str] = "EXECUTED") -> Iterable[list]:
    """Функция принимает на вход список словарей с данными о банковских операциях и параметр state, возвращает новый
    список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение."""
    return [i for i in my_list if i["state"] == state]


def sort_by_date(my_list: Union[list], sort_descending: Union[bool] = True) -> Union[list]:
    """Функция принимает на вход список словарей и параметр порядка сортировки, возвращает новый список,
    в котором исходные словари отсортированы по дате."""
    return sorted(my_list, key=lambda x: x["date"], reverse=sort_descending)
