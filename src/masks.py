from typing import Optional


def get_mask_card_number(number_card: Optional[int] = None) -> str:
    """
    Функция выдает макску карты в формате: XXXX XX** **** XXXX
    :param number_card:
    :return:
    """
    if type(number_card) is not int:
        raise TypeError("Номер карты может быть только числовым значением!")
    if number_card < 0:
        raise ValueError("Номер карты не может быть отрицальным!")
    mask_number_card_str = str(number_card)
    if len(mask_number_card_str) == 16:
        return f"{mask_number_card_str[:4]} {mask_number_card_str[4:6]}** **** {mask_number_card_str[12:]}"
    else:
        raise ValueError("Номер карты состоит не из 16 цифр!")


def get_mask_account(number_account: Optional[int] = None) -> str:
    """
    Функция выдает макску счета в формате: **XXXX
    :param number_account:
    :return:
    """
    if type(number_account) is not int:
        raise TypeError("Номер счёта может быть только числовым значением!")
    if number_account < 0:
        raise ValueError("Номер счёта не может быть отрицальным!")
    mask_number_account_str = str(number_account)
    if len(mask_number_account_str) >= 6:
        return f"**{mask_number_account_str[-4:]}"
    else:
        raise ValueError("Номер счёта не может быть меньше 6 цифт!")
