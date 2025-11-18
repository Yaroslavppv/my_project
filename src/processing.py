def filter_by_state(user_list_dict: list, state: str = "EXECUTED") -> list:
    """
    Функция сортирует данные по ключу операции 'state'.
    :param user_list_dict: список словарей для сортировки
    :param state: ключ 'state' для сортировки
    :return: отсортированный список
    """
    new_list = []
    for el in user_list_dict:
        if el["state"] == state:
            new_list.append(el)
    return new_list


def sort_by_date(user_list_dict: list, descending: bool = True) -> list:
    """
    Функция сортирует данные по дате.
    :param user_list_dict: список словарей для сортировки
    :param descending: порядок сортировки (По умолчанию -  по убыванию)
    :return: отсортированный список
    """
    new_list = sorted(user_list_dict, key=lambda date: date["date"], reverse=descending)
    return new_list
