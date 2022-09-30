# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('N = '))
list = []
fac = 1
for i in range(1, num + 1):
    fac *= i
    list.append(fac)

print(f'Пусть N = {num}, тогда {list}')