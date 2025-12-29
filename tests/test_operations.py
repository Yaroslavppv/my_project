import pytest

from src.operations import process_bank_operations, process_bank_search


@pytest.mark.parametrize(
    "test_dict, test_search, test_answer, expected, exception_message",
    [
        (1, 1, None, TypeError, "Словарь операций должен быть словарем!"),
        ("1", 1, None, TypeError, "Строка поиска должна быть в формате строки!"),
        (
            [
                {
                    "id": 27192367,
                    "state": "CANCELED",
                    "date": "2018-12-24T20:16:18.819037",
                    "operationAmount": {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 71687416928274675290",
                    "to": "Счет 87448526688763159781",
                },
                {
                    "id": 121646999,
                    "state": "CANCELED",
                    "date": "2018-06-08T16:14:59.936274",
                    "operationAmount": {"amount": "91121.62", "currency": {"name": "руб.", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Maestro 7552745726849311",
                    "to": "Счет 34799481846914116850",
                },
            ],
            "Перевод со счета",
            [
                {
                    "id": 27192367,
                    "state": "CANCELED",
                    "date": "2018-12-24T20:16:18.819037",
                    "operationAmount": {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 71687416928274675290",
                    "to": "Счет 87448526688763159781",
                }
            ],
            None,
            None,
        ),
    ],
)
def test_process_bank_search(test_dict, test_search, test_answer, expected, exception_message):
    if expected is not None:
        with pytest.raises(expected) as exc_info:
            process_bank_search(test_dict, test_search)
            assert str(exc_info.value) == exception_message
    else:
        assert process_bank_search(test_dict, test_search) == test_answer


@pytest.mark.parametrize(
    "test_dict, test_list, test_answer, expected, exception_message",
    [
        (1, 1, None, TypeError, "Словарь операций должен быть словарем!"),
        ("1", 1, None, TypeError, "Категории поиска должны быть в формате списка!"),
        (
            [
                {
                    "id": 27192367,
                    "state": "CANCELED",
                    "date": "2018-12-24T20:16:18.819037",
                    "operationAmount": {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 71687416928274675290",
                    "to": "Счет 87448526688763159781",
                },
                {
                    "id": 121646999,
                    "state": "CANCELED",
                    "date": "2018-06-08T16:14:59.936274",
                    "operationAmount": {"amount": "91121.62", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 7552745726849311",
                    "to": "Счет 34799481846914116850",
                },
                {
                    "id": 176798279,
                    "state": "CANCELED",
                    "date": "2019-04-18T11:22:18.800453",
                    "operationAmount": {"amount": "73778.48", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 90417871337969064865",
                },
            ],
            ["Открытие вклада"],
            {"Открытие вклада": 1},
            None,
            None,
        ),
    ],
)
def test_process_bank_operations(test_dict, test_list, test_answer, expected, exception_message):
    if expected is not None:
        with pytest.raises(expected) as exc_info:
            process_bank_search(test_dict, test_list)
            assert str(exc_info.value) == exception_message
    else:
        assert process_bank_operations(test_dict, test_list) == test_answer
