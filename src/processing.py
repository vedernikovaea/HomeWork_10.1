def filter_by_state(data, state='EXECUTED') -> list[str]:
    """
    Функция принимает список словарей  и возвращает те,
    у которых ключ соответвует указанному значению
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data, reverse=True) -> list[str]:
    """
    Функция принимает список словарей и параметр,
    задающий порядок сортировки и возвращает новый
    список, откортированный по дате
    """
    return sorted(data, key=lambda x: x.get('date', ''), reverse=reverse)
