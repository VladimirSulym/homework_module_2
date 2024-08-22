from typing import Optional, Union


def get_mask_card_number(card_number: Union[str, int]) -> Optional[str]:
    """Функция принимает на вход номер карты в виде строки или числа и возвращает ее маску."""
    if card_number and len(str(card_number)) == 16 and str(card_number).isdigit():
        str_to_list = list(str(card_number))
        # заменяем цифры с 6 по 11 на *
        for i in [6, 7, 8, 9, 10, 11]:
            str_to_list[i] = "*"
        # вставляем необходимые пробелы в позиции 4, 9, 14
        for i in [4, 9, 14]:
            str_to_list.insert(i, " ")
        return "".join(str_to_list)
    else:
        return None


def get_mask_account(account_number: Union[str, int]) -> Optional[str]:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if account_number and len(str(account_number)) == 20 and str(account_number).isdigit():
        return "**" + str(account_number)[-4::1]
    else:
        return None
