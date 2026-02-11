import pytest
from src.generators import card_number_generator


@pytest.mark.parametrize("start,end,expected_error,error_message", [
    # start < 1
    (0, 5, ValueError, "Диапазон должен быть от 1 до 9999999999999999"),
    (-1, 10, ValueError, "Диапазон должен быть от 1 до 9999999999999999"),
    (-100, -50, ValueError, "Диапазон должен быть от 1 до 9999999999999999"),

    # end > максимального значения
    (1, 10000000000000000, ValueError, "Диапазон должен быть от 1 до 9999999999999999"),
    (500, 99999999999999999, ValueError, "Диапазон должен быть от 1 до 9999999999999999"),

    # start > end
    (10, 5, ValueError, "Начальное значение не может быть больше конечного"),
    (100, 1, ValueError, "Начальное значение не может быть больше конечного"),
    (9999999999999999, 1, ValueError, "Начальное значение не может быть больше конечного"),

    # Оба значения вне диапазона
    (0, 10000000000000000, ValueError, "Диапазон должен быть от 1 до 9999999999999999"),
    (-1, 10000000000000001, ValueError, "Диапазон должен быть от 1 до 9999999999999999"),
])
def test_card_number_generator_invalid_inputs(start, end, expected_error, error_message):
    """Тест обработки недопустимых входных данных"""
    # Act & Assert
    with pytest.raises(expected_error) as exc_info:
        list(card_number_generator(start, end))

    # Проверяем текст ошибки
    assert error_message in str(exc_info.value), \
        f"Ожидалось сообщение '{error_message}', получено '{exc_info.value}'"


def test_minimum_boundary():
    """Тест минимально допустимого значения (1)"""
    # Act
    generator = card_number_generator(1, 1)
    result = next(generator)

    # Assert
    assert result == "0000 0000 0000 0001", \
        f"Минимальный номер карты должен быть '0000 0000 0000 0001', получен '{result}'"

    # Проверяем, что генератор завершается после одного элемента
    with pytest.raises(StopIteration):
        next(generator)


def test_maximum_boundary():
    """Тест максимально допустимого значения (9999999999999999)"""
    # Act
    generator = card_number_generator(9999999999999999, 9999999999999999)
    result = next(generator)

    # Assert
    assert result == "9999 9999 9999 9999", \
        f"Максимальный номер карты должен быть '9999 9999 9999 9999', получен '{result}'"

    # Проверяем, что после цифры 9 следующей не будет (переполнение)
    with pytest.raises(StopIteration):
        next(generator)
