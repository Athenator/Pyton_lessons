# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
# __str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.

class Worker:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Имя и фамилия рабочего -  {self.name} {self.surname} (реализация: __str__)'

    base = 0
    bonus = 0
    __income = {'base': base, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Имя и фамилия рабочего: {self.name} {self.surname}')

    def get_total_income(self, position):
        if position == 'Каменщик':
            Worker.base = 15250
            Worker.bonus = 29420
        if position == 'Жестянщик':
            Worker.base = 13500
            Worker.bonus = 24860
        if position == 'Упаковщик':
            Worker.base = 10200
            Worker.bonus = 20260
        print(f'Полная заработная плата на должности {position}: {Worker.base + Worker.bonus} рублей')


a = Position('Сергей', 'Иванов')
print(a)
a.get_full_name()
a.get_total_income('Каменщик')

c = Position('Михаил', 'Безруков')
c.get_full_name()
c.get_total_income('Жестянщик')

b = Position('Владимир', 'Чернышев')
b.get_full_name()
b.get_total_income('Упаковщик')
