import requests
from dotenv import load_dotenv
import os


def currency_to_rub(amount: float, currency: str) -> float:
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {"to":"RUB", "from":currency, "amount":amount}

    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers, params=payload)

    status_code = response.status_code
    result = response.json()

    if status_code == 200:
        return result
    else:
        print(f"Запрос не был успешным. Возможная причина: {response.reason}")