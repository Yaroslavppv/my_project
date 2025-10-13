from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == '7000 79** **** 6361'

    assert get_mask_card_number(21314) == 'Номер карты состоит не из 16 цифр!'

    assert get_mask_card_number(12345678901234567890) == 'Номер карты состоит не из 16 цифр!'

    assert get_mask_card_number(-1231) == "Номер карты не может быть отрицальным!"

    assert get_mask_card_number(-1234567890123456) == "Номер карты не может быть отрицальным!"

    assert get_mask_card_number('Привет') == 'Номер карты может быть только числовым значением!'

    assert get_mask_card_number(True) == 'Номер карты может быть только числовым значением!'

    assert get_mask_card_number() == 'Номер карты может быть только числовым значением!'


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == '**4305'

    assert get_mask_account(123456) == '**3456'

    assert get_mask_account(21316) == "Номер счёта не может быть меньше 6 цифт!"

    assert get_mask_account(-1231) == "Номер счёта не может быть отрицальным!"

    assert get_mask_account(-1234567890123456) == "Номер счёта не может быть отрицальным!"

    assert get_mask_account('Привет') == 'Номер счёта может быть только числовым значением!'

    assert get_mask_account(True) == 'Номер счёта может быть только числовым значением!'

    assert get_mask_account() == 'Номер счёта может быть только числовым значением!'