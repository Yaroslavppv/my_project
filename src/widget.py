from typing import Optional

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(client_data: Optional[str] = None) -> str:
    """
    Функция выдает счет или карту с готовой маской
    :param client_data:
    :return:
    """
    if type(client_data) is not str:
        raise TypeError("Данные могут быть только строкой!")
    letters_list = []
    number_list = []
    for el in client_data:
        if el.isdigit():
            number_list.append(el)
        else:
            letters_list.append(el)
    letters = "".join(letters_list)
    number = "".join(number_list)
    if not letters or not number:
        raise ValueError("Не указан параметр счёт/карта")
    else:
        if "Счет" in letters:
            return f"{letters}{get_mask_account(int(number))}"
        else:
            return f"{letters}{get_mask_card_number(int(number))}"


def get_date(time_date: Optional[str] = None) -> str:
    """
    Функция форматирует дату и время в формат: ДД.ММ.ГГГГ
    :param time_date:
    :return:
    """
    if type(time_date) is not str:
        raise TypeError("Данные могут быть только строкой!")
    if (
        time_date[:4].isdigit()
        and time_date[4] == "-"
        and time_date[5:7].isdigit()
        and time_date[7] == "-"
        and time_date[8:10].isdigit()
    ):
        return f"{time_date[8:10]}.{time_date[5:7]}.{time_date[:4]}"
    else:
        raise ValueError("Неерный формат даты!")
