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