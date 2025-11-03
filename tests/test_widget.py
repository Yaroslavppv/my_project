import pytest

from src.widget import mask_account_card, get_date

def test_mask_account_card():
    with pytest.raises(TypeError) as exc_info:
        mask_account_card()
    assert str(exc_info.value) == "Данные могут быть только строкой!"

    with pytest.raises(TypeError) as exc_info:
        mask_account_card(123)
    assert str(exc_info.value) == "Данные могут быть только строкой!"

    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Maestro")
    assert str(exc_info.value) == "Не указан параметр счёт/карта"

    with pytest.raises(ValueError) as exc_info:
        mask_account_card("1596837868705199")
    assert str(exc_info.value) == "Не указан параметр счёт/карта"

    assert mask_account_card('Maestro 1596837868705199') == "Maestro 1596 83** **** 5199"

    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"

    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"




def test_get_date():
    with pytest.raises(TypeError) as exc_info:
        get_date()
    assert str(exc_info.value) == "Данные могут быть только строкой!"

    with pytest.raises(TypeError) as exc_info:
        get_date(123)
    assert str(exc_info.value) == "Данные могут быть только строкой!"

    with pytest.raises(ValueError) as exc_info:
        get_date("2024.03-11T02:26:18.671407")
    assert str(exc_info.value) == "Неерный формат даты!"

    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"



