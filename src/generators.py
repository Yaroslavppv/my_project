from typing import Iterator


def filter_by_currency(transactions: list, currency_code: str) -> Iterator:
    """
    Функция принимает на вход список словарей и возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)
    :param transactions: Список для обработки
    :param currency_code: Код валюты (RUB, USD)
    :return: Поочередно выдает транзакции
    """
    if not isinstance(transactions, list):
        raise TypeError("Фильтрация возможна только по списку словарей!")
    for record in transactions:
        transactions_currency_code = record.get("operationAmount").get("currency").get("code", "Error")
        if transactions_currency_code == "Error":
            raise ValueError("В списке словарей нет кода валют!")
        elif transactions_currency_code == currency_code:
            yield record


def transaction_descriptions(transactions: list) -> Iterator:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    :param transactions: Список для обработки
    :return: Поочередно выдает операции
    """
    if not isinstance(transactions, list):
        raise TypeError("Фильтрация возможно только по списку словарей!")
    for record in transactions:
        transaction_descriptions_str = record.get("description", "Error")
        if transaction_descriptions_str == "Error":
            raise ValueError("В списке словарей нет описания операции!")
        else:
            yield transaction_descriptions_str


def card_number_generator(start: int, finish: int) -> Iterator:
    """
    Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты
    :param start: Стартовое число
    :param finish: Финишное число
    :return: Поочередно выдает номера карт по заданому интервалу
    """
    if not isinstance(start, int) or not isinstance(finish, int):
        raise TypeError("Начало и конец генерации могут быть только числами!")
    elif finish <= start:
        raise ValueError("Конечный параметр не может быть меньше или равен начальному!")
    elif start < 0:
        raise ValueError("Стартовое число не может быть меньше 0!")
    elif finish > 9999999999999999:
        raise ValueError("Финишное число не может быть больше 9999999999999999!")
    while start != finish + 1:
        card_number_str = str(start).zfill(16)
        card_number_str = (
            f"{card_number_str[:4]} {card_number_str[4:8]} {card_number_str[8:12]} {card_number_str[12:16]}"
        )
        start += 1
        yield card_number_str
