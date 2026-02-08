from src.processing import filter_by_state
import pytest


@pytest.fixture
def sample_data():
    """Фикстура с тестовыми данными"""
    return [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "PENDING", "amount": 200},
        {"id": 3, "state": "EXECUTED", "amount": 300},
        {"id": 4, "state": "CANCELED", "amount": 400},
        {"id": 5, "state": "PENDING", "amount": 500},
        {"id": 6, "state": "EXECUTED", "amount": 600},
        {"id": 7, "state": "FAILED", "amount": 700},
        {"id": 8},  # без ключа 'state'
    ]


@pytest.mark.parametrize("state,expected_ids", [
    ("EXECUTED", [1, 3, 6]),
    ("PENDING", [2, 5]),
    ("CANCELED", [4]),
    ("FAILED", [7]),
    ("UNKNOWN", []),  # несуществующий статус
    ("executed", []),  # регистр важен
    ("", []),  # пустой статус
])
def test_filter_by_state_different_states(sample_data, state, expected_ids):
    """Тестирование фильтрации по разным статусам"""
    result = filter_by_state(sample_data, state)
    assert [item["id"] for item in result] == expected_ids


def test_filter_by_state_default(sample_data):
    """Тестирование фильтрации по умолчанию (EXECUTED)"""
    result = filter_by_state(sample_data)
    assert len(result) == 3
    assert all(item["state"] == "EXECUTED" for item in result)
    assert [item["id"] for item in result] == [1, 3, 6]


def test_filter_by_state_empty_list():
    """Тест с пустым списком на входе"""
    result = filter_by_state([])
    assert result == []
    assert len(result) == 0
