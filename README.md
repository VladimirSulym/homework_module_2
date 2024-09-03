# Проект Новый видже для клиента
## Описание:
Проект Новый видже для клиента - это виджет, который показывает несколько последних успешных банковских операций клиента.
## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/VladimirSulym/homework_module_2.git
```
2. Установите зависимости:
```
poetry install
```
3. Запуск тестирования:
```
pytest
```
## Использование:
1. Проект на стадии разработки, информация будет позже.
2. Для всех реализованных функций написаны docstring.
3. В программе реализовано тестирование. Все тесты лежат в папке tests. 
4. Созданы инструменты для эффективной работы с большими объемами данных транзакций.
Генераторы позволяют финансовым аналитикам быстро и удобно находить нужную информацию о транзакциях и 
проводить анализ данных. Для этого создан модуль generators, который содержит функции для работы 
с массивами транзакций.
5. Разработан декоратор log, который автоматически регистрирует детали выполнения функций, 
имя функции, передаваемые аргументы, результат выполнения и информация об ошибках. 
Это позволит обеспечить более глубокий контроль и анализ поведения программы в процессе ее выполнения.
6. В качестве входных данных для многих функций теперь можно использовать данные, полученные из JSON-файла.
7. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют 
и конвертации суммы операции в рубли. Для конвертации валюты используется Exchange Rates Data API
8. Написано логирование модулей masks.py и utils.py. Все логи из этих модулей сохраняются в файл [application.log](logs/application.log) 

## Документация:
Для получения дополнительной информации обратитесь к [документации](README.md).
## Лицензия:
Этот проект лицензирован по [лицензии MIT](LICENSE).