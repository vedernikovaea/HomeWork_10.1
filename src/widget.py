def mask_account_card(user_number_1: str) -> str:
    """Принимает номер карты или счета и выводит ее маску"""
    user_number = str(user_number_1)

    # Извлекаем все цифры из строки
    digits = ''.join(filter(str.isdigit, user_number))
    count_digits = len(digits)

    if count_digits not in (16, 20):
        return "Введите корректный номер Вашей карты или счета"

    # Извлекаем нецифровую часть (название карты или "Счет")
    non_digits = ''.join(filter(lambda x: not x.isdigit(), user_number)).strip()

    if count_digits == 20:
        mask = f"**{digits[-4:]}"
        return f'Счет {mask}'

    elif count_digits == 16:
        # Формируем маску для 16-значного номера
        masked_digits = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
        if non_digits:
            return f'{non_digits} {masked_digits}'
        else:
            return masked_digits
