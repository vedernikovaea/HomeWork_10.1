import functools

def log(filename=None):
    """
    Декоратор для логирования вызова функции.
    Если filename указан, лог пишется в файл, иначе в консоль.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
                message = f"{func_name} ok"
            except Exception as e:
                # Формируем сообщение об ошибке
                error_type = type(e).__name__
                args_str = str(tuple(args)) if args else "()"
                kwargs_str = str(kwargs) if kwargs else "{}"
                message = f"{func_name} error: {error_type}. Inputs: {args_str }, {kwargs_str }"
                # Логируем ошибку
                _log(message, filename)
                raise  # повторно возбуждаем исключение
            else:
                # Логируем успех
                _log(message, filename)
                return result
        return wrapper

    # Обработка случая @log (без вызова)
    if callable(filename):
        func = filename
        filename = None
        return decorator(func)

    return decorator

def _log(message, filename):
    """Записывает сообщение в файл или печатает в консоль."""
    if filename:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    else:
        print(message)