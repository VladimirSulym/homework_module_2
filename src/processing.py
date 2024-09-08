"""Модул содержит 2 функции работы о словарями"""

from typing import Union


def filter_by_state(my_list: Union[list], state: Union[str] = "EXECUTED") -> Union[list, None]:
    """Функция принимает на вход список словарей с данными о банковских операциях и параметр state, возвращает новый
    список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение."""
    if my_list and state in ["CANCELED", "EXECUTED", None]:
        try:
            if state is None:
                state = "EXECUTED"
            # формируем новый список и сразу проверяем словарь на соответствие шаблону данных, если он не соответствует
            # то он не попадает в результирующий список
            result = [i for i in my_list if (i["state"] == str(state)) and (set(i.keys()) == {"id", "state", "date"})]
        except KeyError:
            result = None
        return result
    else:
        return None


def sort_by_date(my_list: Union[list], sort_descending: Union[bool] = True) -> Union[list, None]:
    """Функция принимает на вход список словарей и параметр порядка сортировки, возвращает новый список,
    в котором исходные словари отсортированы по дате."""
    if my_list and sort_descending in [True, False, None]:
        if sort_descending is None:
            sort_descending = True
        # удаляем из списка словарь, содержащий не полные данные и формируем новый список для сортировки
        new_list = [i for i in my_list if set(i.keys()) == {"id", "state", "date"}]
        # сортируем список
        return sorted(new_list, key=lambda x: x["date"], reverse=sort_descending)
    else:
        return None
