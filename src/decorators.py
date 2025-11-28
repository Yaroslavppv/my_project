import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для запись логов испольнения функции
    :param filename: файл для записи (по умолчанию выводить в консоль)
    :return:
    """

    def write_log(message: Any) -> Any:
        if filename:
            with open(filename, "a", encoding="utf-8") as file:
                message = f"{message}\n"
                return file.write(message)

        else:
            return print(message)

    def decorator(function: Callable) -> Callable:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message_start = f"Функция {function.__name__} начинает выполняться."
            write_log(log_message_start)
            try:
                result = function(*args, **kwargs)
                log_message_end = f"{function.__name__} успешно выполнена. Результат: {result}"
                write_log(log_message_end)
                return result
            except Exception as error:
                log_message_end = (
                    f"{function.__name__} выдает ошибку: {type(error).__name__}. Параметры: {args}, {kwargs}."
                )
                write_log(log_message_end)

        return wrapper

    return decorator
