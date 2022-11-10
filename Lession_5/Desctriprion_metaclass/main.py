class Check:
    @classmethod
    def integ(cls, value):
        if type(value) != int:
            raise TypeError('Значение величины, должно быть цифрой!')

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        self.integ(value)
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class ReadLenth:
    def __set_name__(self, owner, name):
        self.name = '__lenth'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class GuardAndCheck:
    @classmethod
    def integ(cls, value):
        if type(value) != int:
            raise TypeError('Значение величины, должно быть цифрой!')

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        self.integ(value)
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = '__' + my_attr


class Road:
    # Дескриптор Check - проверяет является ли значение цифрой.
    # GuardAndCheck - защищает атрибут и проверяет значение.
    # ReadLenth - считывание данных.
    lenth = GuardAndCheck()
    width = GuardAndCheck()
    asfl = Check()
    canvas = Check()
    lr = ReadLenth()

    def __init__(self, lenth, width, asfl, canvas):
        self.lenth = lenth
        self.width = width
        self.asfl = asfl
        self.canvas = canvas
        res = lenth * width * asfl * canvas
        print(f'{lenth}м * {width}м * {asfl}кг * {canvas}м = {res} кг')


r = Road(10, 10, 10, 10)
r.lr = 10
print(r.__dict__)
