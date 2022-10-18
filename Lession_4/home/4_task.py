# Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
# speed, color, name, is_police (булево).
# А также публичные методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс публичный метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar передопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    is_Police = False
    if is_Police:
        is_Police = f'Это полицейский автомобиль '
    else:
        is_Police = f'Это не полицейский автомобиль '

    def __init__(self, speed, color, name):
        self.speed = f'Максимальная скорость: {speed} км в час'
        self.color = f'Цвет автомобиля: {color}'
        self.name = f'Название автомобиля: {name}'

    def go(self):
        return print(f'Автомобиль поехал')

    def stop(self):
        print(f'Автомобиль остановился\n'
              f'---------------------------------------------------')

    def turn(self, direction):
        print(f'Автомобиль повернул {direction}')

    def show_speed(self, now_speed):
        print(f'Сейчас автомобиль движется со скоростью: {now_speed} км/час')


class WorkCar(Car):
    def show_speed(self, now_speed):
        if now_speed >= 40:
            print(f'Сейчас автомобиль движется со скоростью: {now_speed} км/час, вы превысили скорость!')
        else:
            print(f'Сейчас автомобиль движется со скоростью: {now_speed} км/час')


class TownCar(Car):
    def show_speed(self, now_speed):
        if now_speed >= 60:
            print(f'Сейчас автомобиль движется со скоростью: {now_speed} км/час, вы превысили скорость!')
        else:
            print(f'Сейчас автомобиль движется со скоростью: {now_speed} км/час')


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_Police = True
    if is_Police:
        is_Police = f'Это полицейский автомобиль '
    pass


wc = WorkCar(160, 'Red', 'Lexus')
print(wc.speed)
print(wc.color)
print(wc.name)
print(wc.is_Police)
wc.go()
wc.show_speed(42)
wc.turn('направо')
wc.stop()

tc = TownCar(140, 'White', 'Mercedes')
print(tc.speed)
print(tc.color)
print(tc.name)
print(tc.is_Police)
tc.go()
tc.show_speed(62)
tc.turn('на разворот')
tc.stop()

sc = SportCar(220, 'Grey', 'BMW')
print(sc.speed)
print(sc.color)
print(sc.name)
print(sc.is_Police)
sc.go()
sc.show_speed(90)
sc.turn('влево')
sc.stop()

pc = PoliceCar(200, 'White and blue', 'Ford')
print(pc.speed)
print(pc.color)
print(pc.name)
print(pc.is_Police)
pc.go()
pc.show_speed(80)
pc.turn('назад')
pc.stop()
