# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

# Домашнее задание семинара 12
# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import logging
import argparse

logging.basicConfig(filename=f'homework.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


class FIOCheck:
    """Check string to be capitalize and alphabetical."""
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        if value and value[0] == value[0].upper() and value.isalpha():
            setattr(instance, self.param_name, value)
        elif value != '':
            msg = 'Must be capitalized and alphabetical.'
            logger.error(msg)
            raise ValueError(msg)

    def __delete__(self, instance):
        msg = f'Свойство "{self.param_name}" нельзя удалять'
        logger.error(msg)
        raise AttributeError(msg)


class Student:
    """
    Contains surname, name, patronymic, grades for subjects and marks for tests.
    Returns info about student.
    """
    surname = FIOCheck()
    name = FIOCheck()
    patronymic = FIOCheck()

    def __init__(self, surname: str, name: str, patronymic: str):
        import csv
        self.subjects = []
        self.grades = {}
        self.tests = {}
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        try:
            with open('subjects_list.csv', 'r', newline='') as f:
                subjects = csv.reader(f, dialect='excel')
                for line in subjects:
                    self.subjects.append(', '.join(line))
        except IOError as e:
            logger.error(e)

    def give_grade(self, subject: str, grade: int):
        """Set grade for subject."""
        if subject not in self.subjects:
            logger.info('Unknown subject.')
            return
        if grade < 2 or grade > 5:
            logger.info('Grade out of range.')
            return
        self.grades.setdefault(subject, []).append(grade)

    def mark_test(self, subject: str, mark: int):
        """Set mark for test."""
        if subject not in self.subjects:
            logger.info('Unknown subject.')
            return
        if mark < 0 or mark > 100:
            logger.info('Mark out of range.')
            return
        self.tests.setdefault(subject, []).append(mark)

    def __str__(self):
        import statistics
        tests = ''
        sum1 = 0
        len1 = 0
        mean_grade = 0.0
        for subject, mark in self.tests.items():
            tests = f'{tests}\n{subject}: {statistics.mean(mark)}'
        for _, grade in self.grades.items():
            sum1 += sum(grade)
            len1 += len(grade)
            mean_grade = sum1 / len1
        return f'{self.surname} {self.name} {self.patronymic}\n' \
               f'{tests}\nСредний балл по предметам: {mean_grade}'


def parse_args():
    parser = argparse.ArgumentParser(description='Get arguments')
    parser.add_argument('-s', '--surname')
    parser.add_argument('-n', '--name')
    parser.add_argument('-p', '--patronymic', default=None)

    arguments = parser.parse_args()

    return Student(arguments.s, arguments.n, arguments.p)


if __name__ == '__main__':
    s1 = Student('Petrov', 'Ivan', 'Igorevich')
    s1.give_grade('Geometry', 4)
    s1.give_grade('Algebra', 4)
    s1.give_grade('History', 5)
    s1.give_grade('Statistics', 5)
    s1.mark_test('Algebra', 55)
    s1.mark_test('Algebra', 70)
    s1.mark_test('Chemistry', 68)
    s1.mark_test('History', 20)
    s1.mark_test('History', 80)
    s1.mark_test('History', 75)
    s1.mark_test('Statistics', 88)

    print(s1)
