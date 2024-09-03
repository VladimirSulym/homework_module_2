import logging
import os
from typing import Optional, Union

from config import LOGS_PATH

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - Modul: %(filename)s - LogName: %(name)s => %(levelname)s: %(message)s",
    filename=os.path.join(LOGS_PATH, "application.log"),
    filemode="a",
)

masks_logger = logging.getLogger("app.masks")
masks_logger.info("Прямой запуск модуля masks.py")


def get_mask_card_number(card_number: Union[str, int]) -> Optional[str]:
    """Функция принимает на вход номер карты в виде строки или числа и возвращает ее маску."""
    masks_logger.info("Запущена функция get_mask_card_number")
    if card_number and len(str(card_number)) == 16 and str(card_number).isdigit():
        masks_logger.info("Получен правильный номер карты")
        str_to_list = list(str(card_number))
        # заменяем цифры с 6 по 11 на *
        for i in [6, 7, 8, 9, 10, 11]:
            masks_logger.debug(f"Замена {i} цифры в номере карты")
            str_to_list[i] = "*"
        # вставляем необходимые пробелы в позиции 4, 9, 14
        for i in [4, 9, 14]:
            masks_logger.debug(f"Вставка пробела в позицию {i}")
            str_to_list.insert(i, " ")
        masks_logger.info("Маска для карты создана")
        masks_logger.info("Функция get_mask_card_number завершила свою работу положительно")
        return "".join(str_to_list)
    else:
        masks_logger.error("Получен не валидный номер карты")
        masks_logger.warning("Функция get_mask_card_number завершила работу с ошибкой")
        return None


def get_mask_account(account_number: Union[str, int]) -> Optional[str]:
    """Функция принимает на вход номер счета и возвращает его маску."""
    masks_logger.info("Запущена функция get_mask_account")
    if account_number and len(str(account_number)) == 20 and str(account_number).isdigit():
        masks_logger.info("Получен правильный номер счета")
        masks_logger.info("Функция get_mask_account завершила свою работу положительно")
        return "**" + str(account_number)[-4::1]
    else:
        masks_logger.error("Получен не валидный номер счета")
        masks_logger.warning("Функция get_mask_account завершила свою работу с ошибкой")
        return None


# if __name__ == '__main__':
#     get_mask_card_number(7000792289602361)
#     get_mask_account("35383033474478695560")
#
