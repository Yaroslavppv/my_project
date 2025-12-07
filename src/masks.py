from typing import Optional

from pathlib import Path
import logging

log_file = Path(__file__).parent.parent / "logs" / "masks.log"

logging.basicConfig(level=logging.DEBUG,
                    encoding="utf-8",
                    format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s',
                    filename=log_file,  # Запись логов в файл
                    filemode='w')

masks_logger = logging.getLogger("masks_logger")

def get_mask_card_number(number_card: Optional[int] = None) -> str:
    """
    Функция выдает макску карты в формате: XXXX XX** **** XXXX
    :param number_card:
    :return:
    """
    masks_logger.info("Функция запущена")
    if type(number_card) is not int:
        masks_logger.error('Номер карты может быть только числовым значением!')
        raise TypeError("Номер карты может быть только числовым значением!")
    if number_card < 0:
        masks_logger.error('Номер карты не может быть отрицальным!')
        raise ValueError("Номер карты не может быть отрицальным!")
    mask_number_card_str = str(number_card)
    if len(mask_number_card_str) == 16:
        masks_logger.info('Функция выполнена успешно')
        return f"{mask_number_card_str[:4]} {mask_number_card_str[4:6]}** **** {mask_number_card_str[12:]}"
    else:
        masks_logger.error('Номер карты состоит не из 16 цифр!')
        raise ValueError("Номер карты состоит не из 16 цифр!")


def get_mask_account(number_account: Optional[int] = None) -> str:
    """
    Функция выдает макску счета в формате: **XXXX
    :param number_account:
    :return:
    """
    masks_logger.info("Функция запущена")
    if type(number_account) is not int:
        masks_logger.error('Номер счёта может быть только числовым значением!')
        raise TypeError("Номер счёта может быть только числовым значением!")
    if number_account < 0:
        masks_logger.error('Номер счёта не может быть отрицальным!')
        raise ValueError("Номер счёта не может быть отрицальным!")
    mask_number_account_str = str(number_account)
    if len(mask_number_account_str) >= 6:
        masks_logger.info('Функция выполнена успешно')
        return f"**{mask_number_account_str[-4:]}"
    else:
        masks_logger.error('Номер счёта не может быть меньше 6 цифр!')
        raise ValueError("Номер счёта не может быть меньше 6 цифр!")
