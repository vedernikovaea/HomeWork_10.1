import pytest

from src.processing import sort_by_date


@pytest.mark.parametrize("reverse, expected_order", [
    (True, ['A', 'B', 'C', 'D', 'E']),  # По убыванию
    (False, ['A', 'B', 'C', 'D', 'E']),  # По возрастанию
])
def test_stable_sorting_with_same_dates(reverse, expected_order):
    """Параметризованный тест стабильной сортировки с одинаковыми датами"""
    data = [
        {'date': '2023-01-01', 'id': 'A'},
        {'date': '2023-01-01', 'id': 'B'},
        {'date': '2023-01-01', 'id': 'C'},
        {'date': '2023-01-01', 'id': 'D'},
        {'date': '2023-01-01', 'id': 'E'},
    ]

    result = sort_by_date(data, reverse=reverse)
    result_order = [item['id'] for item in result]
    assert result_order == expected_order
