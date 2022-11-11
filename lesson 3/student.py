import datetime


class Student:
    name = ''
    birth_year = 0
    group = ''
    mark = .0

    def __init__(self, name='', birth_year=0, group='', mark=0):
        self.name = name
        self.birth_year=birth_year
        self.group = group
        self.mark = mark

    def __str__(self):
        return f'== {self.name} ==\n' \
               f'Год рождения: {self.birth_year}\n' \
               f'Класс: {self.group}\n' \
               f'Ср. оценка: {self.mark}\n'

    def get_age(self):
        return datetime.date.today().year - self.birth_year