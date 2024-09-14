import os

from config import DATA_PATH
from src.processing import filter_by_state, sort_by_date
from src.read_csv_xlsx import convert_csv_to_list, convert_xlsx_to_list
from src.search import transaction_search
from src.utils import get_data_json
from src.widget import get_date, mask_account_card

# словарь для хранения выбранных опций пользователя
user_config = {
    "main_menu": None,
    "second_menu": [
        ["Отсортировать операции по дате?", "Да", "Нет", None],
        ["Отсортировать по возрастанию или по убыванию?", "По убыванию", "По возрастанию", None],
        ["Выводить только рублевые транзакции?", "Да", "Нет", None],
        ["Отфильтровать список транзакций по определенному слову в описании?", "Да", "Нет", None],
    ],
    "status": None,
}


def main():
    """Функция, запускающая само приложение выдающая основное меню"""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    user_config["main_menu"] = input("Введите пункт меню => ")
    # условный оператор, который согласно выбору пользователя запускает функции чтения файлов и получения из них
    # информации
    match user_config["main_menu"]:
        case "1":
            print("Для обработки выбран JSON-файл.")
            get_status()
            second_menu()
            path_json = os.path.join(DATA_PATH, "operations.json")
            data_json = get_data_json(path_json)
            data_filter = filter_by_state(data_json, user_config["status"])
            user_config_operations(data_filter)
        case "2":
            print("Для обработки выбран CSV-файл.")
            get_status()
            second_menu()
            path_csv = os.path.join(DATA_PATH, "transactions.csv")
            data_csv = convert_csv_to_list(path_csv)
            data_filter = filter_by_state(data_csv, user_config["status"])
            user_config_operations(data_filter)
        case "3":
            print("Для обработки выбран XLSX-файл.")
            get_status()
            second_menu()
            path_xlsx = os.path.join(DATA_PATH, "transactions_excel.xlsx")
            data_xlsx = convert_xlsx_to_list(path_xlsx)
            data_filter = filter_by_state(data_xlsx, user_config["status"])
            user_config_operations(data_filter)
        case _:
            print(f"Пункт {user_config['main_menu']} в меню отсутствует")


def get_status():
    """Функция запрашивает статус фильтрации у пользователя, проверяет его валидность и сохраняет результат в
    конфигурации пользователя"""
    while user_config["status"] is None:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        input_user = input("Введите статус => ").upper()
        if input_user not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {input_user} недоступен.")
        else:
            print(f"Операции отфильтрованы по статусу {input_user}")
            user_config["status"] = input_user


def user_config_operations(data_filter):
    """Функция, которая вызывает вспомогательные функции, согласно конфигурации пользователя и выводит на экран
    результат всей работы"""
    for index, value in enumerate(user_config["second_menu"]):
        match index:
            case 0:
                if value[3]:
                    data_filter = sort_by_date(data_filter, user_config["second_menu"][index + 1][3])
            case 2:
                if value[3]:
                    data_filter = transaction_search(data_filter, "RUB")
            case 3:
                if value[3]:
                    data_filter = transaction_search(data_filter, input("Введите слово для фильтрации => "))
    if len(data_filter):
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(data_filter)}\n")
        for my_dict in data_filter:
            print(f'{get_date(my_dict['date'])} {my_dict["description"]}')
            if my_dict["description"] == "Перевод с карты на карту":
                print(f"{mask_account_card(my_dict['from'])} -> {mask_account_card(my_dict['to'])}")
            elif my_dict["description"] == "Открытие вклада":
                print(f"{mask_account_card(my_dict['to'])}")
            elif my_dict["description"] == "Перевод организации":
                print(f"{mask_account_card(my_dict['from'])} -> {mask_account_card(my_dict['to'])}")
            elif my_dict["description"] == "Перевод со счета на счет":
                print(f"{mask_account_card(my_dict['from'])} -> {mask_account_card(my_dict['to'])}")
            if user_config["main_menu"] == "1":
                print(f"{my_dict['operationAmount']['amount']} {my_dict['operationAmount']['currency']['code']}\n")
            else:
                print(f"{my_dict['amount']} {my_dict['currency_code']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def second_menu():
    """Функция, которая запрашивает у пользователя конфигурацию обработки данных и сохраняет ее
    в переменную user_config"""
    print("Выборка операций:")
    for index, value in enumerate(user_config["second_menu"]):
        if index != 1:
            print(value[0], value[1], value[2])
            input_user = input().lower()
            if input_user == value[1].lower():
                value[3] = True
            elif input_user == value[2].lower():
                value[3] = False
        else:
            if user_config["second_menu"][index - 1][3]:
                print(value[0], value[1], value[2])
                input_user = input().lower()
                if input_user == value[1].lower():
                    value[3] = True
                elif input_user == value[2].lower():
                    value[3] = False

    # print(user_config)
    # print(user_config['status'])


if __name__ == "__main__":
    main()
