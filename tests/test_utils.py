from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

import src.utils as utils

absolute_path = Path(__file__).parent.parent / "data" / "operations.json"


@pytest.mark.parametrize(
    "test_transactions, expected_output, expected, exception_message, mock_test, mock_data, mock_captured",
    [
        (1, None, TypeError, "Файл должен быть указан в формате строки!", None, None, None),
        ("1", [], None, None, None, None, None),
        (None, None, None, None, True, "", f"Не удалось декодировать JSON из файла: {absolute_path}\n"),
        (None, None, None, None, True, "{}", f"Файл {absolute_path} не содержить список!\n"),
    ],
)
def test_get_transactions(
    capsys, test_transactions, expected_output, expected, exception_message, mock_test, mock_data, mock_captured
):
    if expected is not None:
        with pytest.raises(expected) as exc_info:
            utils.get_transactions(test_transactions)
        assert str(exc_info.value) == exception_message
    elif mock_test:
        with patch("builtins.open", mock_open(read_data=mock_data)) as m:
            utils.get_transactions(str(absolute_path))
            m.assert_called_with(absolute_path, "r", encoding="utf-8")
            captured = capsys.readouterr()
            assert captured.out == mock_captured
    else:
        assert utils.get_transactions(test_transactions) == expected_output


@pytest.mark.parametrize(
    "test_transactions, expected_output, expected, exception_message, mock_test",
    [
        (1, None, TypeError, "transaction должен быть словарем!", None),
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            31957.58,
            None,
            None,
            None,
        ),
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "3", "currency": {"name": "руб.", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            229.1,
            None,
            None,
            True,
        ),
    ],
)
def test_get_transaction_amount(test_transactions, expected_output, expected, exception_message, mock_test):
    if expected is not None:
        with pytest.raises(expected) as exc_info:
            utils.get_transaction_amount(test_transactions)
        assert str(exc_info.value) == exception_message
    elif mock_test:
        with (
            patch("src.utils.get_transaction_amount", return_value=229.1) as mock_transaction_amount,
            patch("src.utils.currency_to_rub", return_value=229.1),
        ):
            assert utils.get_transaction_amount(test_transactions) == expected_output
            mock_transaction_amount.assert_called_once_with(test_transactions)
    else:
        assert utils.get_transaction_amount(test_transactions) == expected_output
