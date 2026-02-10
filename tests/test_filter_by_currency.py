import pytest
from src.generators import filter_by_currency

@pytest.fixture
def sample_transactions():
    """Фикстура: базовый набор тестовых транзакций"""
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "доллар США", "code": "USD"}
            }
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет",
            "operationAmount": {
                "amount": "200.00",
                "currency": {"name": "доллар США", "code": "USD"}
            }
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту",
            "operationAmount": {
                "amount": "300.00",
                "currency": {"name": "евро", "code": "EUR"}
            }
        },
        {
            "id": 4,
            "description": "Оплата услуг",
            "operationAmount": {
                "amount": "400.00",
                "currency": {"name": "российский рубль", "code": "RUB"}
            }
        },
        {
            "id": 5,
            "description": "Покупка в магазине",
            "operationAmount": {
                "amount": "500.00",
                "currency": {"name": "доллар США", "code": "USD"}
            }
        },
    ]


@pytest.mark.parametrize("currency,expected_ids", [
    ("USD", [1, 2, 5]),  # 3 транзакции в USD
    ("EUR", [3]),  # 1 транзакция в EUR
    ("RUB", [4]),  # 1 транзакция в RUB
    ("GBP", []),  # Нет транзакций в GBP
])
def test_filter_by_currency_basic(sample_transactions, currency, expected_ids):
    """Параметризованный тест базовой фильтрации по валюте"""
    # Act
    result = list(filter_by_currency(sample_transactions, currency))

    # Assert
    result_ids = [t["id"] for t in result]
    assert result_ids == expected_ids, \
        f"Для валюты {currency} ожидались ID: {expected_ids}, получены: {result_ids}"

    # Дополнительно проверяем описания для найденных транзакций
    for transaction in result:
        assert "description" in transaction
        assert "operationAmount" in transaction



