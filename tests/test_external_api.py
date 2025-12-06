import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import currency_to_rub


@patch("requests.get")
def test_currency_to_rub(mock_get):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    base_url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": API_KEY}
    params = {"to": "RUB", "from": "USD", "amount": 1.0}

    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 1},
        "info": {"timestamp": 1765007823, "rate": 76.80419},
        "date": "2025-12-06",
        "result": 76.80419,
    }
    mock_get.return_value.status_code = 200
    assert currency_to_rub(1.0, "USD") == {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 1},
        "info": {"timestamp": 1765007823, "rate": 76.80419},
        "date": "2025-12-06",
        "result": 76.80419,
    }
    mock_get.assert_called_once_with(base_url, headers=headers, params=params)
