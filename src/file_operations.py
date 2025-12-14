import csv
import logging
from pathlib import Path

import pandas as pd

log_file = Path(__file__).parent.parent / "logs" / "file_operations.log"

logging.basicConfig(
    level=logging.DEBUG,
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s",
    filename=log_file,  # Запись логов в файл
    filemode="w",
)

file_operations_logger = logging.getLogger("file_operations_logger")


def csv_read_operations(csv_file: str):
    """
    Функция считывает финансовые операции из CSV файла
    :param csv_file: путь до csv файла
    :return: возвращает словарь с транзакциями
    """
    file_operations_logger.info("Функция запущена")
    if not isinstance(csv_file, str):
        file_operations_logger.error("Файл должен быть указан в формате строки!")
        raise TypeError("Файл должен быть указан в формате строки!")
    try:
        with open(csv_file, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            data_operations = []
            for row in reader:
                data_operations.append(row)
            file_operations_logger.info("Функция успешно выполнена")
            return data_operations
    except FileNotFoundError:
        file_operations_logger.error(f"Файл {csv_file} не найден!")
        raise FileNotFoundError(f"Файл {csv_file} не найден!")


def excel_read_operation(excel_file: str):
    """
    Функция считывает финансовые операции из EXCEL файла
    :param excel_file: путь до excel файла
    :return: возвращает словарь с транзакциями
    """
    file_operations_logger.info("Функция запущена")
    if not isinstance(excel_file, str):
        file_operations_logger.error("Файл должен быть указан в формате строки!")
        raise TypeError("Файл должен быть указан в формате строки!")
    try:
        data_operations = pd.read_excel(excel_file)
        if data_operations.empty:
            file_operations_logger.error("Файл пустой или содержит только заголовок")
            raise StopIteration("Файл пустой или содержит только заголовок")
        return data_operations.to_dict()
    except FileNotFoundError:
        file_operations_logger.error(f"Файл {excel_file} не найден!")
        raise FileNotFoundError(f"Файл {excel_file} не найден!")
