from typing import Optional, Union


def get_mask_card_number(card_number: Union[str, int]) -> Optional[str]:
    """Функция принимает на вход номер карты в виде строки или числа и возвращает ее маску."""
    str_to_list = list(str(card_number))
    # заменяем цифры с 6 по 11 на *
    for i in [6, 7, 8, 9, 10, 11]:
        str_to_list[i] = "*"
    # вставляем необходимые пробелы в позиции 4, 9, 14
    for i in [4, 9, 14]:
        str_to_list.insert(i, " ")
    return "".join(str_to_list)


def get_mask_account(account_number: Union[str, int]) -> Optional[str]:
    """Функция принимает на вход номер счета и возвращает его маску."""
    return "**" + str(account_number)[-4::1]
