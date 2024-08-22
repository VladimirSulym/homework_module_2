"""Этот модуль содержит функции для работы с новыми возможностями приложения."""

from typing import Optional, Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: Union[str]) -> Optional[str]:
    """Маскирует счет или номер карты"""
    if isinstance(account_card_info, str):
        # считаем кол-во цифр и определяем - счет или карта
        if account_card_info[-17] == " " and account_card_info[-16:].isdigit():
            return str(account_card_info[:-17] + " " + get_mask_card_number(account_card_info[-16:]))
        elif account_card_info[-21] == " " and account_card_info[-20:].isdigit():
            return str(account_card_info[:-21] + " " + get_mask_account(account_card_info[-20:]))
        else:
            return None
    return None


def get_date(my_date: Union[str]) -> Optional[str]:
    """Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ" ("11.03.2024")"""
    if isinstance(my_date, str) and my_date and my_date[4] == "-" and my_date[7] == "-":
        print(my_date)
        if my_date[:10].replace("-", "").isdigit():
            return ".".join(list(reversed(my_date[:10].split("-"))))
    else:
        return None
