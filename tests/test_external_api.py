from src.external_api import currency_conversion
import os
from dotenv import load_dotenv
from unittest.mock import patch

load_dotenv()


@patch("requests.get")
def test_currency_conversion(mock_get):
    mock_get.return_value.json.return_value = {"result": 2.00}
    assert currency_conversion("USD", 2) == 2.00
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": os.getenv("API_KEY")},
        params={
            "to": "RUB",
            "from": "USD",
            "amount": "2",
        },
    )
