# 📌 Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# 📌 *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые, т.е не мая, а 5.
from datetime import datetime
import logging
import argparse

logging.basicConfig(filename=f'date.log',
                    encoding='utf-8',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)
days_of_week = ['пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос']
months = ['', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн',
              'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']


def string_to_date(string_entry: str):
    try:
        week, day, month = string_entry.lower().split()
    except ValueError as e:
        logger.info(e)
        return None

    week_num = int(week[0])
    weekday = days_of_week.index(day[:3])
    month = months.index(month[:3])
    year = datetime.now().year

    count = 0
    for i in range(1, 32):
        date_ = datetime(day=i, month=month, year=year)
        if date_.weekday() == weekday:
            count += 1
            if count == week_num:
                return date_.date()


def parse_args():
    parser = argparse.ArgumentParser(description='Получаем аргументы')
    parser.add_argument('-w', '--week', default=1)
    parser.add_argument('-d', '--weekday', default=datetime.now().weekday())
    parser.add_argument('-m', '--month', default=datetime.now().month)

    arguments = parser.parse_args()
    month = months[arguments.m] if isinstance(arguments.m, int) else arguments.m
    weekday = days_of_week[arguments.d] if isinstance(arguments.d, int) else arguments.d
    week_num = str(arguments.w) if isinstance(arguments.w, int) else arguments.w
    return string_to_date(f'{week_num} {weekday} {month}')


if __name__ == '__main__':
    # print(string_to_date('1-й четверг ноября'))
    # print(string_to_date('3-я среда мая'))
    # print(string_to_date('5-е воскресенье апреля'))
    print(parse_args())
