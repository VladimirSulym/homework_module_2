import os
from shutil import which

from config import DATA_PATH
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.search import transaction_search
from src.utils import get_data_json

user_config = {
    'main_menu': None,
    'second_menu': [
        ['Отсортировать операции по дате?', 'Да', 'Нет', None],
        ['Отсортировать по возрастанию или по убыванию?', 'По убыванию', 'По возрастанию', None],
        ['Выводить только рублевые тразакции?', 'Да', 'Нет', None],
        ['Отфильтровать список транзакций по определенному слову в описании?', 'Да', 'Нет', None]
    ],
    'status': None
}

def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n'
          'Выберите необходимый пункт меню:\n'
          '1. Получить информацию о транзакциях из JSON-файла\n'
          '2. Получить информацию о транзакциях из CSV-файла\n'
          '3. Получить информацию о транзакциях из XLSX-файла')
    user_config['main_menu'] = input('Введите пункт меню => ')
    match user_config['main_menu']:
        case '1':
            print('Для обработки выбран JSON-файл.')
            get_status()
            second_menu()
            path_json = os.path.join(DATA_PATH, "operations.json")
            data_json = get_data_json(path_json)
            # print(type(data_json))
            # print(data_json)
            # print(data_json[0].keys())
            data_filter = filter_by_state(data_json, user_config['status'])
            for index, value in enumerate(user_config['second_menu']):
                # print('value =>', value)
                # print('value =>', value[3])
                match index:
                    case 0:
                        if value[3]:
                            data_filter = sort_by_date(data_filter, user_config['second_menu'][index + 1][3])
                            # print(data_filter)
                    case 2:
                        if value[3]:
                            data_filter = transaction_search(data_filter, "RUB")
                            # print(data_filter)
                    case 3:
                        if value[3]:
                            data_filter = transaction_search(data_filter, input('Введите слово для фильтрации => '))
                            # print(data_filter)
            print(data_filter)
        case '2':
            print('Для обработки выбран CSV-файла.')
            get_status()
            second_menu()
        case '3':
            print('Для обработки выбран XLSX-файла.')
            get_status()
            second_menu()
        case _:
            print(f'Пункт {user_config['main_menu']} в меню отсутствует')

def get_status():
    while user_config['status'] is None:
        print('Введите статус, по которому необходимо выполнить фильтрацию.\n'
              'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        input_user = input('Введите статус => ').upper()
        if input_user not in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Статус операции {input_user} недоступен.')
        else:
            print(f'Операции отфильтрованы по статусу {input_user}')
            user_config['status'] = input_user


def second_menu():
    print('Выборка операций:')
    for index, value in enumerate(user_config['second_menu']):
        if index != 1:
            print(value[0], value[1], value[2])
            input_user = input().lower()
            if input_user == value[1].lower():
                value[3] = True
            elif input_user == value[2].lower():
                value[3] = False
        else:
            if user_config['second_menu'][index - 1][3]:
                print(value[0], value[1], value[2])
                input_user = input().lower()
                if input_user == value[1].lower():
                    value[3] = True
                elif input_user == value[2].lower():
                    value[3] = False

    # print(user_config)
    # print(user_config['status'])

if __name__ == '__main__':
    main()