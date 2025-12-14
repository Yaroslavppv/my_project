from pathlib import Path
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.file_operations import csv_read_operations, excel_read_operation

csv_file = Path(__file__).parent.parent / "data" / "transactions.csv"
excel_file = Path(__file__).parent.parent / "data" / "transactions_excel.xlsx"


@pytest.mark.parametrize(
    "expected, file, return_message, mock_test, mock_data",
    [
        (TypeError, 123, "Файл должен быть указан в формате строки!", None, None),
        (None, csv_file, [], True, "id;state;date;amount;currency_name;currency_code;from;to;description"),
        (FileNotFoundError, "ads.csv", "Файл ads.csv не найден!", None, None),
        (
            None,
            csv_file,
            [
                {
                    "id": "650703",
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": "16210",
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                }
            ],
            True,
            "id;state;date;amount;currency_name;currency_code;from;to;description\n"
            "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;"
            "Счет 39745660563456619397;Перевод организации",
        ),
    ],
)
def test_csv_read_operations(expected, file, return_message, mock_test, mock_data):
    if expected is not None and mock_test is not True:
        with pytest.raises(expected) as exc_info:
            csv_read_operations(file)
        assert str(exc_info.value) == return_message
    elif mock_test:
        with patch("builtins.open", mock_open(read_data=mock_data)) as m:
            result = csv_read_operations(str(file))
            assert result == return_message
            m.assert_called_with(str(Path(file)), encoding="utf-8")


@pytest.mark.parametrize(
    "expected, file, return_message, mock_test, mock_data",
    [
        (TypeError, 123, "Файл должен быть указан в формате строки!", None, None),
        (StopIteration, excel_file, "Файл пустой или содержит только заголовок", True, [{}]),
        (FileNotFoundError, "ads.csv", "Файл ads.csv не найден!", None, None),
        (
            None,
            excel_file,
            {
                "id": {0: 650703},
                "state": {0: "EXECUTED"},
                "date": {0: "2023-09-05T11:30:32Z"},
                "amount": {0: 16210},
                "currency_name": {0: "Sol"},
                "currency_code": {0: "PEN"},
                "from": {0: "Счет 58803664561298323391"},
                "to": {0: "Счет 39745660563456619397"},
                "description": {0: "Перевод организации"},
            },
            True,
            [
                {
                    "id": 650703,
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": 16210,
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                }
            ],
        ),
    ],
)
def test_excel_read_operation(expected, file, return_message, mock_test, mock_data):
    if expected is not None and mock_test is not True:
        with pytest.raises(expected) as exc_info:
            excel_read_operation(file)
        assert str(exc_info.value) == return_message
    elif mock_test and expected:
        mock_dataframe = pd.DataFrame(mock_data)
        with patch("pandas.read_excel", return_value=mock_dataframe):
            with pytest.raises(expected) as exc_info:
                excel_read_operation(str(file))
            assert str(exc_info.value) == return_message
    elif mock_test:
        mock_dataframe = pd.DataFrame(mock_data)
        with patch("pandas.read_excel", return_value=mock_dataframe) as mock_read:
            result = excel_read_operation(str(file))
            assert result == return_message
            mock_read.assert_called_once_with(str(Path(file)))
