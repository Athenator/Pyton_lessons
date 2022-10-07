# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#  45 -> 101101
#  3 -> 11
#  2 -> 10

# Через bin
# num = int(input('Введите число: '))
# num_double = bin(num)
# print(num_double[2:])


# Через алгоритм

num = int(input('Введите число: '))
num_d = ''

while num > 0:
    num_d = str(num % 2) + num_d
    num //= 2
print(num_d)