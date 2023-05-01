# 📌 Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.
import logging

logging.basicConfig(filename='task01logs.log', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


def create_error(a: int, b: int = 0) -> str:
    try:
        result = a / b
        result = f'{result = }'
    except ZeroDivisionError as e:
        logger.error(e)
        result = e
    return result


if __name__ == '__main__':
    print(create_error(5, 2))
    print(create_error(5, 0))
