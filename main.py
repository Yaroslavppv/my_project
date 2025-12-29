import os.path

import src.file_operations
import src.operations
import src.processing
import src.utils
import src.widget

BASE_DIR = os.path.dirname(__file__)
path_file = {
    1: BASE_DIR + "/data/operations.json",
    2: BASE_DIR + "/data/transactions.csv",
    3: BASE_DIR + "/data/transactions_excel.xlsx",
}
return_dict = {
    1: "Для обработки выбран JSON-файл",
    2: "Для обработки выбран CSV-файл",
    3: "Для обработки выбран XLSX-файл",
}
from_file = {1: "json", 2: "csv", 3: "xlsx"}

dict_file = {
    1: src.utils.get_transactions(path_file[1]),
    2: src.file_operations.csv_read_operations(path_file[2]),
    3: src.file_operations.excel_read_operation(path_file[3]),
}


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    transactions = []
    user_input_file = None
    while True:
        try:
            print(
                "Выберите необходимый пункт меню:\n"
                "1. Получить информацию о транзакциях из JSON-файла\n"
                "2. Получить информацию о транзакциях из CSV-файла\n"
                "3. Получить информацию о транзакциях из XLSX-файла\n"
            )
            user_input_file = int(input())
            if user_input_file in (1, 2, 3):
                print(return_dict[user_input_file])
                transactions = dict_file[user_input_file]
                break
        except ValueError:
            continue

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        user_input = input().upper()
        if user_input in ("EXECUTED", "CANCELED", "PENDING"):
            transactions = src.processing.filter_by_state(transactions, user_input)
            print(f"Операции отфильтрованы по статусу {user_input}")
            break
        else:
            print(f'Статус операции "{user_input}" недоступен.')
            continue

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию")
                user_input = input().lower()
                if user_input == "по убыванию":
                    transactions = src.processing.sort_by_date(transactions)
                    break
                elif user_input == "по возрастанию":
                    transactions = src.processing.sort_by_date(transactions, False)
                    break
                else:
                    continue
            break
        elif user_input == "нет":
            break
        else:
            continue

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            transactions = src.processing.filter_by_currency(transactions, from_file[user_input_file])
            break
        elif user_input == "нет":
            break
        else:
            continue

    while True:
        print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            while True:
                print("Введите слово для поиска")
                user_input = input()
                transactions = src.operations.process_bank_search(transactions, user_input)
                break
            break
        elif user_input == "нет":
            break
        else:
            continue

    print("Распечатываю итоговый список транзакций...")
    if len(transactions):
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for el in transactions:
            print(el)
            print(f'{src.widget.get_date(el["date"])} {el["description"]}')
            if el["description"] == "Открытие вклада":
                print(f'{src.widget.mask_account_card(el["to"])}')
            else:
                print(f'{src.widget.mask_account_card(el["from"])} -> {src.widget.mask_account_card(el["to"])}')
            print(
                f'Сумма: {el["operationAmount"]["amount"] if user_input_file == 1 else el["amount"]} '
                f'{el["operationAmount"]["currency"]["name"] if user_input_file == 1 else el["currency_name"]}\n'
            )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
