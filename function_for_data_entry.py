def get_input(prompt, converter=float):
    """Универсальная функция для ввода данных"""
    return converter(input(prompt))
