# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответствует формату.
from datetime import datetime
import logging

logging.basicConfig(filename=f'date.log',
                    encoding='utf-8',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)


def string_to_date(string_entry: str):
    days_of_week = {'пон': 0, 'вто': 1, 'сре': 2,
                    'чет': 3, 'пят': 4, 'суб': 5, 'вос': 6}
    months = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4,
              'мая': 5, 'июн': 6, 'июл': 7, 'авг': 8,
              'сен': 9, 'окт': 10, 'ноя': 11, 'дек': 12}
    try:
        week, day, month = string_entry.lower().split()
    except ValueError as e:
        logger.info(e)

    week_num = int(week[0])
    weekday = days_of_week[day[:3]]
    month = months[month[:3]]
    year = datetime.now().year

    count = 0
    for i in range(1, 32):
        date_ = datetime(day=i, month=month, year=year)
        if date_.weekday() == weekday:
            count += 1
            if count == week_num:
                return date_.date()


if __name__ == '__main__':
    print(string_to_date('1-й четверг ноября'))
    print(string_to_date('3-я среда мая'))
    print(string_to_date('5-е воскресенье апреля'))
