import os
import re
from collections import Counter

from config import DATA_PATH
from src.read_csv_xlsx import convert_csv_to_list

def transaction_search(dicts_trans: list, search_str: str) -> list:
    """ Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых есть данные в записях совпадающие с данной строкой. Функция осуществляет
    поиск по всем полям и возвращает максимально подходящие варианты ответа в зависимости от степени совпадения данных"""
    search_str_list = re.findall(r"[^\d\W][a-zA-Zа-яА-Я\s]+[^\W\d]|[a-zA-Zа-яА-Я]", search_str, flags=re.IGNORECASE | re.DOTALL)
    search_int_list = re.findall(r"\d+\W\d+\W\d+|\d+", search_str, flags=re.IGNORECASE | re.DOTALL)
    # print(search_str_list)
    # print(search_int_list)
    result =[]
    for dict_trans in dicts_trans:
        for key, value in dict_trans.items():
            if search_int_list:
                for i in search_int_list:
                    if str(value).strip().find(i) != -1:
                        result.append(dict_trans)
            if search_str_list:
                for i in search_str_list:
                    if str(value).strip().find(i) != -1:
                        result.append(dict_trans)
    result_filter = []
    flag_set = set()
    flag_rank = 2
    for i in result:
        temp = tuple(i.items())
        if result.count(i) == flag_rank:
            if temp not in flag_set:
                flag_set.add(temp)
                result_filter.append(i)
        elif result.count(i) > flag_rank:
            flag_rank = result.count(i)
            flag_set.add(temp)
            result_filter = [i]
    if result_filter:
        return result_filter
    else:
        return result

# transaction_search(convert_csv_to_list(os.path.join(DATA_PATH, "transactions.csv")),"Euro")

for i in transaction_search(convert_csv_to_list(os.path.join(DATA_PATH, "transactions.csv")),"ОткрыТие вКЛада, EUR, 79277383088424042634")[:]:
    print(i)