# 📌 Доработаем задачу 2.
# 📌 Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.
from typing import Callable
import logging

logging.basicConfig(filename=f'my_func.log',
                    encoding='utf-8', format='{levelname} - {asctime}: {msg}',
                    style='{', level=logging.INFO)
logger = logging.getLogger(__name__)


def deco(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        my_dict = {'args': args, **kwargs}

        message = f'{func.__name__} {my_dict} {result}'

        logger.info(message)
        return result

    return wrapper


@deco
def my_func(*args, **kwargs) -> str:
    return f'Функция отработала.'


if __name__ == '__main__':
    my_func(52, 2, 11, 6, tora=5, bible=14)
