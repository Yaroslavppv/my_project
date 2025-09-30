from typing import Optional


def get_mask_card_number(number_card: Optional[int] = None) -> str:
    """
    Функция выдает макску карты в формате: XXXX XX** **** XXXX
    :param number_card:
    :return:
    """
    mask_number_card_str = str(number_card)
    return f"{mask_number_card_str[:4]} {mask_number_card_str[4:6]}** **** {mask_number_card_str[13:]}"


def get_mask_account(number_account: Optional[int] = None) -> str:
    """
    Функция выдает макску счета в формате: **XXXX
    :param number_account:
    :return:
    """
    mask_number_account_str = str(number_account)
    return f"**{mask_number_account_str[-4:]}"
