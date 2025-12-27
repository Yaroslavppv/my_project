import logging
import re
from collections import Counter
from pathlib import Path

log_file = Path(__file__).parent.parent / "logs" / "operations.log"

logging.basicConfig(
    level=logging.DEBUG,
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s",
    filename=log_file,  # Запись логов в файл
    filemode="w",
)

operations_logger = logging.getLogger("operations_logger")


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка
    :param data: Словарь с данными
    :param search: Строка поиска
    :return: Список словарей в которых есть данная строка
    """
    operations_logger.info("Функция запущена")
    if not isinstance(search, str):
        operations_logger.error("Строка поиска должна быть в формате строки!")
        raise TypeError("Строка поиска должна быть в формате строки!")
    if not isinstance(data, list):
        operations_logger.error("Словарь операций должен быть словарем!")
        raise TypeError("Словарь операций должен быть словарем!")

    list_operations = []
    for operation in data:
        if re.search(search, operation["description"]):
            list_operations.append(operation)

    operations_logger.info("Функция выполнена успешно")
    return list_operations


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    :param data: Список словарей с данными о банковских операциях
    :param categories: Список категорий операций [description]
    :return: Количество операций в каждой категории
    """
    operations_logger.info("Функция запущена")
    if not isinstance(categories, list):
        operations_logger.error("Категории поиска должны быть в формате списка!")
        raise TypeError("Категории поиска должны быть в формате списка!")
    if not isinstance(data, list):
        operations_logger.error("Словарь операций должен быть словарем!")
        raise TypeError("Словарь операций должен быть словарем!")

    dict_operations = []
    for el in data:
        if el.get("description") in categories:
            dict_operations.append(el["description"])
    counter = Counter(dict_operations)

    operations_logger.info("Функция выполнена успешно")
    return dict(counter)
