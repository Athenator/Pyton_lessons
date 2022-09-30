# Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число
import random

num = int(input('Введите число: '))
List = []
for i in range(-num,num+1):
    List.append(i)

with open('file.txt', 'w') as data:
    count_num = random.randrange(1,num)
    for _ in range(0, count_num):
        mass =  random.randint(-num, num+1)
        with open('file.txt', 'a') as data:
             data.write(f'{mass}\n')

pos = 1
with open('file.txt', 'r') as data:
    for j in data:
        pos *= List[int(j)]
        


print(List)
print(f'Произведение позиций: {pos}')