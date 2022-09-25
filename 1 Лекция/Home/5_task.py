# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
def inputXY(x):
    x = int(input('Введите координату Х: '))
    y = int(input('Введите координату Y: '))
    xy = [x, y]
    return xy


def lengthAB(a, b):
    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return length


print("Введите координаты точки А")
A = inputXY(2)
print("Введите координаты точки В")
B = inputXY(2)

print(f"Расстояние: {format(lengthAB(A, B), '.2f')}")