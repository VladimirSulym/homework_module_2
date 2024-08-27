from unittest.mock import patch

from src.external_api import currency_conversion


@patch("os.getenv")
@patch("requests.get")
def test_currency_conversion(mock_get, mock_getenv):
    mock_get.return_value.json.return_value = {"result": 2.00}
    mock_getenv.return_value = "123"
    assert currency_conversion("USD", 2) == 2.00
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "123"},
        params={
            "to": "RUB",
            "from": "USD",
            "amount": "2",
        },
    )
