import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number("Привет")
    assert str(exc_info.value) == "Номер карты может быть только числовым значением!"

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(True)
    assert str(exc_info.value) == "Номер карты может быть только числовым значением!"

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number()
    assert str(exc_info.value) == "Номер карты может быть только числовым значением!"

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(-1231)
    assert str(exc_info.value) == "Номер карты не может быть отрицальным!"

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(12345678901234567890)
    assert str(exc_info.value) == "Номер карты состоит не из 16 цифр!"

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(21314)
    assert str(exc_info.value) == "Номер карты состоит не из 16 цифр!"

    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_account():
    with pytest.raises(TypeError) as exc_info:
        get_mask_account("Привет")
    assert str(exc_info.value) == "Номер счёта может быть только числовым значением!"

    with pytest.raises(TypeError) as exc_info:
        get_mask_account()
    assert str(exc_info.value) == "Номер счёта может быть только числовым значением!"

    with pytest.raises(TypeError) as exc_info:
        get_mask_account(True)
    assert str(exc_info.value) == "Номер счёта может быть только числовым значением!"

    with pytest.raises(ValueError) as exc_info:
        get_mask_account(-1231)
    assert str(exc_info.value) == "Номер счёта не может быть отрицальным!"

    with pytest.raises(ValueError) as exc_info:
        get_mask_account(21314)
    assert str(exc_info.value) == "Номер счёта не может быть меньше 6 цифр!"

    assert get_mask_account(73654108430135874305) == "**4305"

    assert get_mask_account(123456) == "**3456"
