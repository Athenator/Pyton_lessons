#  Вывести квадрат числа 
# number = int(input('Введите число: '))
# print(f'Квадрат числа {number} равен {number**2}')


# Проверить, являестя одно число квадратом другого
# a = int(input('a = '))
# b = int(input('b = '))
# print(f'{a}, {b} ->', end = ' ')
# if a == b**2 or b == a**2:
#     print('Да')
# else:
#     print('Нет')

# Найти максимальное из 5 чисел 
# list = [int(input('a = ')), int(input('b = ')), int(input('c = ')), int(input('d = ')), int(input('f = '))]
# max = list[0]
# for i in list:
#     if max < i:
#         max = i

# print(f'{list} -> {max}')


# Напишите программу, которая на вход принимает число N и выводит числа от -N до N 
# n = abs(int(input('N = ')))
# for i in range(-n,n+1):
#     print(i,end=' ')

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части
# a = float(input('A = '))
# b = int(a * 10 % 10)
# if b == 0:
#     print(f'{a} - > Нет')
# else:
#     print(f'{a} - > {b}')

# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15 но не 30.

c = int(input('C = '))

if ((c % 5== 0 and c % 10 == 0) or c % 15 == 0) and c % 30 != 0:
    print('кратно 5 и 10 или 15, но не 30')
else:
    print('Нет')