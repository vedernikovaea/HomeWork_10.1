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

    return "Неизвестный формат карты"




def get_date(date_str: str) -> str:
    """Принимает строку  и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    # Извлекаем часть строки с датой (до символа 'T')
    date_part = date_str.split('T')[0]

    # Разделяем дату на компоненты и переставляем их
    year, month, day = date_part.split('-')

    # Форматируем в нужный вид
    return f"{day}.{month}.{year}"




if __name__ == "__main__":
    '''Тестирование функции mask_account_card'''
    print(mask_account_card('Maestro 1596837868705199'))
    print(mask_account_card('Счет 64686473678894779589'))
    print(mask_account_card('MasterCard 7158300734726758'))
    print(mask_account_card('Счет 35383033474447895560'))
    print(mask_account_card('Visa Classic 6831982476737658'))
    print(mask_account_card('Visa Platinum 8990922113665229'))
    print(mask_account_card('Visa Gold 5999414228426353'))
    print(mask_account_card('Счет 73654108430135874305'))

    '''Тестирование get_date'''
    print(get_date("2024-03-11T02:26:18.671407"))  # Вернет: 11.03.2024
    print(get_date("2023-12-25T15:30:45.123456"))  # Вернет: 25.12.2023
