import json
from pathlib import Path

from src.external_api import currency_to_rub


def get_transactions(filepath: str) -> list[dict]:
    """
    Функция, принимающая на вход путь до JSON-файла и возвращающая список словарей с данными о финансовых транзакциях
    :param filepath: путь до файла
    :return: возвращает список транзакций
    """
    if not isinstance(filepath, str):
        raise TypeError("Файл должен быть указан в формате строки!")
    pathfile = Path(filepath)

    try:
        with open(pathfile, "r", encoding="utf-8") as file:
            data_transactions = json.load(file)
            if not isinstance(data_transactions, list):
                print(f"Файл {filepath} не содержить список!")
                return []
            return data_transactions

    except json.JSONDecodeError:
        print(f"Не удалось декодировать JSON из файла: {filepath}")
        return []
    except FileNotFoundError:
        print(f"Файл {filepath} не найден!")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка при чтении файла: {e}")
        return []


def get_transaction_amount(transaction: dict) -> float:
    """
    Функция, принимающая на вход транзакцию и возвращащая сумму транзакции в рублях(RUB)
    :param transaction: транзакия
    :return: возвращает значение в рублях (float)
    """
    if not isinstance(transaction, dict):
        raise TypeError("transaction должен быть словарем!")
    if (
        transaction["operationAmount"]["currency"]["code"] == "USD"
        or transaction["operationAmount"]["currency"]["code"] == "EUR"
    ):
        return round(
            float(
                currency_to_rub(
                    transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"]
                )
            ),
            2,
        )
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        raise ValueError("Такая валюта не подерживается!")
