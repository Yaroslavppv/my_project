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


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        False,
    )
)
