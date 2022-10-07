#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# inp = input('задайте последовательность чисел: ')
# ros = []
# for item in inp:
#     if item not in ros:
#         ros.append(item)
# print(inp)
# print(ros)


# Другое решение 

lst = list(map(int, input('Введите числа ')))
print(f'Исходный список {lst}')
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
new_lst.sort()
print(f'Список из неповторяющихся элементов: {new_lst}')
