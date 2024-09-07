import os
from unittest.mock import patch

from config import DATA_PATH
from src.read_csv_xlsx import convert_csv_to_list, convert_xlsx_to_list


@patch("pandas.read_csv")
def test_convert_csv_to_list(mock_read):
    mock_read.return_value.to_dict.return_value = 2
    assert convert_csv_to_list(os.path.join(DATA_PATH, "transactions.csv")) == 2
    mock_read.assert_called_once_with(os.path.join(DATA_PATH, "transactions.csv"), delimiter=";")


@patch("pandas.read_excel")
def test_convert_xlsx_to_list(mock_read):
    mock_read.return_value.to_dict.return_value = 3
    assert convert_xlsx_to_list(os.path.join(DATA_PATH, "transactions_excel.xlsx")) == 3
    mock_read.assert_called_once_with(os.path.join(DATA_PATH, "transactions_excel.xlsx"), decimal=";")
