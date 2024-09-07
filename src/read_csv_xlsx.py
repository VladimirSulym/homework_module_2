import pandas


def convert_csv_to_list(path: str) -> list:
    """Функция для считывания финансовых операций из CSV файла и выдает список словарей с транзакциями."""
    df = pandas.read_csv(path, delimiter=";")
    return df.to_dict("records")


def convert_xlsx_to_list(path: str) -> list:
    """Функция для считывания финансовых операций из Excel файла и выдает список словарей с транзакциями."""
    df = pandas.read_excel(path, decimal=";")
    return df.to_dict("records")


# if __name__ == "__main__":
#     print(convert_csv_to_list(os.path.join(DATA_PATH, "transactions.csv")))
#     print(convert_xlsx_to_list(os.path.join(DATA_PATH, "transactions_excel.xlsx")))
