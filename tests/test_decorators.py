from src.decorators import log


def test_log(capsys):
    @log()
    def test_function(x: int, y: int):
        return x + y

    test_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == (
        "Функция test_function начинает выполняться.\n" "test_function успешно выполнена. Результат: 3\n"
    )

    test_function(1)
    captured = capsys.readouterr()
    assert captured.out == (
        "Функция test_function начинает выполняться.\n"
        "test_function выдает ошибку: TypeError. Параметры: (1,), {}.\n"
    )
