import pytest

from src.processing import filter_by_currency, filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "test_user_dict, test_state, test_answer",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(test_user_dict, test_state, test_answer):
    assert filter_by_state(test_user_dict, test_state) == test_answer


def test_sort_by_date():
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        True,
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        False,
    ) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "test_user_dict, test_format, test_currency, test_answer",
    [
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
            "json",
            "RUB",
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
        ),
        (
            [
                {
                    "id": "1652868",
                    "state": "CANCELED",
                    "date": "2020-11-12T21:50:44Z",
                    "amount": "31742",
                    "currency_name": "Ruble",
                    "currency_code": "RUB",
                    "from": "",
                    "to": "Счет 44859048793086957451",
                    "description": "Открытие вклада",
                },
                {
                    "id": "1935024",
                    "state": "CANCELED",
                    "date": "2020-11-18T12:07:03Z",
                    "amount": "13249",
                    "currency_name": "Ruble",
                    "currency_code": "USD",
                    "from": "",
                    "to": "Счет 83739717055666813179",
                    "description": "Открытие вклада",
                },
            ],
            "csv",
            "RUB",
            [
                {
                    "id": "1652868",
                    "state": "CANCELED",
                    "date": "2020-11-12T21:50:44Z",
                    "amount": "31742",
                    "currency_name": "Ruble",
                    "currency_code": "RUB",
                    "from": "",
                    "to": "Счет 44859048793086957451",
                    "description": "Открытие вклада",
                }
            ],
        ),
        (
            [
                {
                    "id": "1652868",
                    "state": "CANCELED",
                    "date": "2020-11-12T21:50:44Z",
                    "amount": "31742",
                    "currency_name": "Ruble",
                    "currency_code": "RUB",
                    "from": "",
                    "to": "Счет 44859048793086957451",
                    "description": "Открытие вклада",
                },
                {
                    "id": "1935024",
                    "state": "CANCELED",
                    "date": "2020-11-18T12:07:03Z",
                    "amount": "13249",
                    "currency_name": "Ruble",
                    "currency_code": "USD",
                    "from": "",
                    "to": "Счет 83739717055666813179",
                    "description": "Открытие вклада",
                },
            ],
            "xlsx",
            "RUB",
            [
                {
                    "id": "1652868",
                    "state": "CANCELED",
                    "date": "2020-11-12T21:50:44Z",
                    "amount": "31742",
                    "currency_name": "Ruble",
                    "currency_code": "RUB",
                    "from": "",
                    "to": "Счет 44859048793086957451",
                    "description": "Открытие вклада",
                }
            ],
        ),
    ],
)
def test_filter_by_currency(test_user_dict, test_format, test_currency, test_answer):
    assert filter_by_currency(test_user_dict, test_format, test_currency) == test_answer
