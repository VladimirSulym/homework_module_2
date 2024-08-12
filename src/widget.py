"""Этот модуль содержит функции для работы с новыми возможностями приложения."""

from typing import Optional

from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> Optional[str]:
    """Маскирует счет или номер карты"""
    # считаем кол-во цифр и определяем - счет или карта
    if account_card_info[-17] == " ":
        return str(account_card_info[:-17] + " " + get_mask_card_number(account_card_info[-16:]))
    else:
        return str(account_card_info[:-21] + " " + get_mask_account(account_card_info[-20:]))
