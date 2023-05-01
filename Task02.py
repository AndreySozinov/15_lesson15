# 📌 На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте модуль logging.
from typing import Callable
import logging


def deco(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        parameters = []

        my_dict = {'args': args, **kwargs, 'result': result}
        parameters.append(my_dict)

        logging.basicConfig(filename=f'{func.__name__}.log', encoding='utf-8', level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info(parameters)
        return result
    return wrapper


@deco
def my_func(*args, **kwargs) -> str:
    return f'Функция отработала.'


if __name__ == '__main__':
    my_func(52, 2, 11, 6, tora=5, bible=14)
