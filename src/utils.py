import json
import logging
from pathlib import Path

from src.external_api import currency_to_rub

log_file = Path(__file__).parent.parent / "logs" / "utils.log"

logging.basicConfig(
    level=logging.DEBUG,
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s",
    filename=log_file,  # Запись логов в файл
    filemode="w",
)

utils_logger = logging.getLogger("masks_logger")


def get_transactions(filepath: str) -> list[dict]:
    """
    Функция, принимающая на вход путь до JSON-файла и возвращающая список словарей с данными о финансовых транзакциях
    :param filepath: путь до файла
    :return: возвращает список транзакций
    """
    utils_logger.info("Функция запущена")
    if not isinstance(filepath, str):
        utils_logger.error("Файл должен быть указан в формате строки!")
        raise TypeError("Файл должен быть указан в формате строки!")
    pathfile = Path(filepath)

    try:
        with open(pathfile, "r", encoding="utf-8") as file:
            data_transactions = json.load(file)
            if not isinstance(data_transactions, list):
                utils_logger.debug(f"Файл {filepath} не содержить список!")
                print(f"Файл {filepath} не содержить список!")
                return []
            utils_logger.info("Функция выполнена успешно")
            return data_transactions

    except json.JSONDecodeError:
        utils_logger.debug(f"Не удалось декодировать JSON из файла: {filepath}")
        print(f"Не удалось декодировать JSON из файла: {filepath}")
        return []
    except FileNotFoundError:
        utils_logger.debug(f"Файл {filepath} не найден!")
        print(f"Файл {filepath} не найден!")
        return []
    except Exception as e:
        utils_logger.debug(f"Произошла непредвиденная ошибка при чтении файла: {e}")
        print(f"Произошла непредвиденная ошибка при чтении файла: {e}")
        return []


def get_transaction_amount(transaction: dict) -> float:
    """
    Функция, принимающая на вход транзакцию и возвращащая сумму транзакции в рублях(RUB)
    :param transaction: транзакия
    :return: возвращает значение в рублях (float)
    """
    utils_logger.info("Функция запущена")
    if not isinstance(transaction, dict):
        utils_logger.error("transaction должен быть словарем!")
        raise TypeError("transaction должен быть словарем!")
    if (
        transaction["operationAmount"]["currency"]["code"] == "USD"
        or transaction["operationAmount"]["currency"]["code"] == "EUR"
    ):
        transaction_amount = round(
            float(
                currency_to_rub(
                    transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"]
                )
            ),
            2,
        )
        utils_logger.info("Функция выполнена успешно")
        return transaction_amount
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        utils_logger.info("Функция выполнена успешно")
        return float(transaction["operationAmount"]["amount"])
    else:
        utils_logger.error("transaction должен быть словарем!")
        raise ValueError("Такая валюта не подерживается!")
