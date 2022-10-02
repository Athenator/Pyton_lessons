# Реализуйте алгоритм перемешивания списка
# import random

# def make_list(array,count):
#     array = []
#     for i in range(count):
#         word = input(f'Введите элемент списка № {i + 1} : ')
#         array.append(word) 
#     return array

# size = int(input('Введите размер списка: '))
# list = []

# list_one = make_list(list,size)
# print(f'Изначальный список: {list_one}')
# random.shuffle(list_one)
# print(f'Список, после перемешивания: {list_one}')
import random
def mix_l(array):
    for i in range(0, len(array)):
        rnd_pos = int(random.randrange(0, len(array)))
        temp = list_or[i]
        list_or[i] = list_or[rnd_pos]
        list_or[rnd_pos] = temp
    return array

num = int(input('Введите колличество элементов в списке: '))
list_or = list([random.randint(10,99)for i in range(0, num)])
print(f'Оригинальный список: {list_or} ')
list_mix = mix_l(list_or)
print(f'Список после перемешивания:{list_mix} ')


# Ещё вариант генерации 
# Реализовать алгоритм перемешивания списка. 
# original = [0, 2, 4, 6, 9] 
# print(original)

# import time


# from time import time

# def time_random():
#     print(time() - float(str(time()).split('.')[0]))
#     return time() - float(str(time()).split('.')[0])


# def random_number(min, max):
#  return int(time_random() * (max - min) + min)

# def mixing_list(array):
#     for i in range(0, len(array)):
#         rnd_position = int(random_number(0, len(array)))
#         temp1 = original[i]
#         original[i] = original[rnd_position]
#         original[rnd_position] = temp1

# mixing_list(original)
# print(original)
