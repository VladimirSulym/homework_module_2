"""Этот модуль содержит функции для работы с новыми возможностями приложения."""
from masks import get_mask_card_number, get_mask_account
from typing import Optional


def mask_account_card(account_card_info: str) -> Optional[str]:
    if account_card_info[-17] == ' ':
        return account_card_info[:-17] + ' ' + get_mask_card_number(account_card_info[-16:])
    else:
        return account_card_info[:-21] + ' ' + get_mask_account(account_card_info[-20:])
