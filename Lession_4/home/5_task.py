# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = None
    def draw(self):
        print(f'Запуск отрисовки ')

class Pen(Stationery):
    title = 'Ручка'
    def draw(self):
        print(f'Запуск отрисовки при помощи ручки\n')


class Pencil(Stationery):
    title = 'Карандаш'
    def draw(self):
        print(f'Запуск отрисовки при помощи карандаша\n')

class Handle(Stationery):
    title = 'Маркер'
    def draw(self):
        print(f'Запуск отрисовки при помощи маркера\n')


pen = Pen()
print(f'Используемый инструмент: {pen.title}')
pen.draw()

pencil = Pencil()
print(f'Используемый инструмент: {pencil.title}')
pencil.draw()

handle = Handle()
print(f'Используемый инструмент: {handle.title}')
handle.draw()