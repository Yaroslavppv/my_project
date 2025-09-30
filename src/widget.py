from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(client_data: str) -> str:
    """
    Функция выдает счет или карту с готовой маской
    :param client_data:
    :return:
    """
    letters_list = []
    number_list = []
    for el in client_data:
        if el.isdigit():
            number_list.append(el)
        else:
            letters_list.append(el)
    letters = "".join(letters_list)
    number = "".join(number_list)
    if "Счет" in letters:
        return f"{letters}{get_mask_account(int(number))}"
    else:
        return f"{letters}{get_mask_card_number(int(number))}"


def get_date(time_date: str) -> str:
    """
    Функция форматирует дату и время в формат: ДД.ММ.ГГГГ
    :param time_date:
    :return:
    """
    return f"{time_date[8:10]}.{time_date[5:7]}.{time_date[:4]}"
