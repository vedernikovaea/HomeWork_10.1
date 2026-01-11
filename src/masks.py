def mask_card(card: str) -> str:
    """Маскирует номер карты"""
    card = card.replace(" ", "")

    if len(card) != 16 or not card.isdigit():
        return "Ошибка: нужен 16-значный номер карты"

    return f"{card[:4]} {card[4:6]}** **** {card[-4:]}"


def mask_account(account: str) -> str:
    """Маскирует номер счета """
    account = account.replace(" ", "")

    if len(account) != 20 or not account.isdigit():
        return "Ошибка: нужен 20-значный номер счета"

    return f"**{account[-4:]}"


# Тестирование
print("Пример карты:")
card = "2200486975594884"
print(f"Было: {card}")
print(f"Стало: {mask_card(card)}")

print("\nПример счета:")
account = "25256698223456298722"
print(f"Было: {account}")
print(f"Стало: {mask_account(account)}")

