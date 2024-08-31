import os
from unittest.mock import patch

from config import DATA_PATH
from src.utils import get_amount_transactions_in_rub, get_data_json


@patch("json.load")
def test_get_data_json(mock_load):
    mock_load.return_value = 2
    assert get_data_json(os.path.join(DATA_PATH, "operations.json")) == 2
    assert get_data_json(None) == []


@patch("src.utils.currency_conversion")
def test_get_amount_transactions_in_rub(mock_conversion):
    mock_conversion.return_value = 1.00
    assert get_amount_transactions_in_rub([]) is None
    assert (
        get_amount_transactions_in_rub(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            }
        )
        == 31957.58
    )

    assert (
        get_amount_transactions_in_rub(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 1.00
    )
