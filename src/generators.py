def filter_by_currency(transactions, currency):
    """Возвращает итератор (генератор) транзакций с заданной валютой.

        transactions: Список словарей с транзакциями
        currency: Код валюты для фильтрации"""
    for transaction in transactions:
        operation_amount = transaction.get('operationAmount', {})
        transaction_currency = operation_amount.get('currency', {}).get('code')

        # Если валюта транзакции совпадает с искомой - возвращаем транзакцию
        if transaction_currency == currency:
            yield transaction




def transaction_descriptions(transactions):
    """Генератор, который возвращает описание каждой транзакции по очереди.
    transactions: Список словарей с транзакциями"""
    for transaction in transactions:
        description = transaction.get('description')
        yield description




def card_number_generator(start: int, end: int):
    """
    Генератор номеров банковских карт в заданном диапазоне.
        start: Начальное значение диапазона (минимально 1)
        end: Конечное значение диапазона (максимально 9999999999999999)"""
    # Проверяем валидность диапазона
    if start < 1 or end > 9999999999999999:
        raise ValueError("Диапазон должен быть от 1 до 9999999999999999")

    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного")

    for number in range(start, end + 1):
        # Форматируем число в строку из 16 цифр с ведущими нулями
        formatted_number = f"{number:016d}"

        # Разбиваем на группы по 4 цифры и объединяем через пробел
        card_number = ' '.join([
            formatted_number[i:i + 4]
            for i in range(0, 16, 4)
        ])

        yield card_number