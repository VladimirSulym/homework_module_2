import json
import os

from config import LOGS_PATH
import logging

from src.external_api import currency_conversion

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - Modul: %(filename)s - LogName: %(name)s => %(levelname)s: %(message)s",
    filename=os.path.join(LOGS_PATH, "application.log"),
    filemode="a",
)

utils_logger = logging.getLogger("app.utils")
utils_logger.info("Прямой запуск модуля utils.py")


def get_data_json(my_path):
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    utils_logger.info("Запущена функция get_data_json")
    try:
        with open(my_path, "r") as f:
            utils_logger.debug(f"Файл {os.path.basename(my_path)} открыт в режиме чтения")
            utils_logger.debug(f"Информация из файла {os.path.basename(my_path)} преобразована в json")
            utils_logger.info("Функция get_data_json завершила работу положительно")
            return json.load(f)
    except Exception as e:
        utils_logger.error(f"Ошибка в функции get_data_json:\n{e}", exc_info=True)
        utils_logger.warning("Функция get_data_json завершила работу с ошибкой")
        return []


def get_amount_transactions_in_rub(transaction):
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    utils_logger.info("Запущена функция get_amount_transactions_in_rub")
    try:
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            utils_logger.debug("Выбранная валюта НЕ рубли")
            utils_logger.info("Функция get_amount_transactions_in_rub завершила работу положительно")
            return currency_conversion(
                transaction["operationAmount"]["currency"]["code"], transaction["operationAmount"]["amount"]
            )
        else:
            utils_logger.debug("Выбранная валюта рубли")
            utils_logger.info("Функция get_amount_transactions_in_rub завершила работу положительно")
            return float(transaction["operationAmount"]["amount"])
    except Exception as e:
        utils_logger.error(f"Ошибка в функции get_amount_transactions_in_rub:\n{e}", exc_info=True)
        utils_logger.warning("Функция get_amount_transactions_in_rub завершила работу с ошибкой")
        return None


# if __name__ == '__main__':
#     base_data = get_data_json(os.path.join(DATA_PATH, "operations.json"))
#     for i in range(10, 15):
#         print(get_amount_transactions_in_rub(base_data[i]))
