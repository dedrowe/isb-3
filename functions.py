import logging


def save_bytes_sequence(text: bytes, file: str) -> None:
    """
    Функция сохраняет бинарную последовательность в файл
    :param text: Последовательность
    :param file: Путь к файлу в который сохраняется последовательность
    :return: Функция ничего не возвращает
    """
    try:
        with open(file, "wb") as f:
            f.write(text)
            logging.info("Бинарная последовательность успешно сохранена")
    except OSError as err:
        logging.warning(f"{err} Не удалось сохранить бинарную последовательность")


def read_bytes_sequence(file: str) -> bytes:
    """
    Фукнция считывает бинарную последовательность из файла
    :param file: Путь к файлу
    :return: Бинарная полседовательность
    """
    try:
        with open(file, 'rb') as f:
            text = f.read()
            logging.info("Бинарная последовательность успешно считан")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать Бинарную последовательность")
    return text
