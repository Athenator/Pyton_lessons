# Задание 2.
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Единственный класс этого проекта — одежда (класс Clothes).
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
# для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать
# абстрактный класс для единственного класса проекта,
# проверить на практике работу декоратора @property
# Пример:
# Расход ткани на пальто = 1.27
# Расход ткани на костюм = 20.30
# Общий расход ткани = 21.57
# Два класса: абстрактный и Clothes

from abc import ABC, abstractmethod


class Cloth(ABC):
    @property
    def jacket(self):
        return str(f'Расход ткани на костюм  \n'
                   f' {round((self.height * 2 + 0.3), 2)}')


class Clothes(Cloth):

    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def coat(self):
        return str(f'Расход ткани на пальто  \n'
                   f' {round((self.width / 6.5 + 0.5),2)}')


    @property
    def all_cloth(self):
        return str(f'Общий расход ткани \n'
                   f' {round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3),2)}')



a = Clothes(10,10)
print(a.coat)
print(a.jacket)
print(a.all_cloth)
