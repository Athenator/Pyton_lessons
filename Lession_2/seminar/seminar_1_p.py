# 19.	Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# import time

# def Random_set(start, end):
#     seconds = time.time()
#     Rand = end * (seconds % 1)

#     return round(Rand)

# print(Random_set(1, 100))

# 20.	Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# a = ['efkdmfmlk445', 'jdfid 94i epr0 0i00ii4u8nfjdf', 'fglk38877 098 mekweir3m']

# Num = int('98')
# def Get_Num_in_List(List,Num):
#     count = 0
#     k = 0
#     for str1 in List:
#         if len(str(Num))>1:
#             for i in range(1,len(str1)):
#                 if str(Num) in str1[k:i]:
#                     count+=1
#                     k=i
#         else:
#             for j in range(len(str1)):
#                 if str1[j]==str(Num):
#                     count+=1
#     return count

# print(Get_Num_in_List(a,Num))


# 21.	Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# def second_in(list, find):
#     count = 0
#     for i in range(len(list)):
#         if list[i] == find:
#             count += 1
#             if count == 2:
#                 return i
#     return -1


# list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# find = "asd"

# print(second_in(list, find))

# Тестирование

# 20.	Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# a = ['efkdmfmlk445', 'jdfid 94i epr0 0i00ii4u8nfjdf', 'fglk38877 098 mekweir3m']
# num1 = 'jd'
# for n in a:
#     if num1 in n:
#         print('True')
#     else:
#         print('False')


# 21.	Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# Строка содержит набор чисел. Показать большее и меньшее число Символ-разделитель - пробел

# ls1 = input('Input: ')
# ls2 = ls1.split(' ')
# print(ls2)
# max = ls2[0]
# min = ls2[0]
# for i in range(len(ls2)):
#     if int(ls2[i]) > int(max): 
#         max = ls2[i]
#     elif int(ls2[i]) < int(min): 
#         min = ls2[i]
# print(f'max number = {max} ; min number = {min}')



# Найти корни квадратного уравнения Ax² + Bx + C = 0 Математикой Используя дополнительные библиотеки*
# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*

# import math

# numA = float(input('Input numA: '))
# numB = float(input('Input numB: '))
# numC = float(input('Input numC: '))

# numD = numB ** 2 - 4 * numA * numC
# print(f'dis = {round(numD, 2)}')

# if numD > 0:
#     x1 = (-numB + math.sqrt(numD)) / (2 * numA)
#     x2 = (-numB - math.sqrt(numD)) / (2 * numA)
#     print(f'x1({round(x1, 2),})')
#     print(f'x1({round(x2, 2)})')
# elif numD == 0:
#     x = -numB / (2 * numA)
#     print(f'x ({round(x, 2)})')
#     print(f'dis = {round(numD, 2)}')
# else:
#     print('There are no sqr')

# Найти НОК двух чисел

# import math

# num1 = int(input('Input number1: '))
# num2 = int(input('Input number2: '))
# num3 = 0
# min = num1
# if num2 < min:
#     min = num2
# num3 = (num1 * num2)// math.gcd(num1, num2)
# print(num3)

# print ('a = ', end = '')
# a = int (input ())
# print ('b = ', end = '')
# b = int (input ())
# p = a * b
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# nod = a + b
# nok = p // nod
# print ('НОК:', nok)
# print ('НОД:', nod)

