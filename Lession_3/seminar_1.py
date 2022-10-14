# @decor
# def check_even_3(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             yield num * num

# def check_even_2(lst):
#     new_list = filter(lambda x: x % 2 == 0, lst)
#     return new_list

# lst = [1, 2, 3, 4, 5, 6]
# d = check_even_2(lst)
# print(list(d))


#  Класссы:
# 1 Создать класс - иссключение от класса Exeprion
# 2 Сгенерировать исключение в нужной точке программы
# 3 отловить и обработать
# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt

# inp_data = input('Введите число: ')

# try:
#     try:
#         inp_data = int(inp_data)
#     except FileExistsError:
#         print('Вы ввели не число!')
#     if inp_data < 0:
#         raise OwnError('Вы ввели отрицательные числа!')
# except OwnError as err:
#     print(err)
# else:
#     print(f'Всё хорошо. Ваше число: {inp_data}')


# from itertools import count
# from math import factorial
# from functools import reduce

# lst = [300, 2, 12, 4, 23, 1, 42, 66, 123, 52, 24,322]
# lst = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]

# lst = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]

# lst = [300, 2, 12, 4, 23, 1, 42, 66, 123, 52, 24,322, 322]
# lst = [el for el in lst if lst.count(el) == 1]

# def fact(n):
#     factorial = 1

#     for x in count(1):
#         if x > n:
#             break
#         factorial = factorial * x
#         yield factorial

# n = int(input('Введите целое число: '))
# i = 0
# for el in fact(n):
#     i += 1
#     print(f'!{i} = {el}')

# lst = [x for x in range(10,101,2)]
# res = reduce(lambda item, item2: item * item2, lst)
# print(res)

# Тестирование

# converted_list = list(map(int, input().split()))
# filter_list = list(filter(lambda x: converted_list.count(x) == 1, converted_list ))
# filtered_list = [x for x in converted_list if x % 2  == 0]
# print(filtered_list)

# a = {n: 3 * n + 1 for n in range(1,5)}
# print(a)

# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# with open ('file.txt', 'r') as data:
#     a = data.read().split()
#     a = list(map(int,a))

# for i in range(1, len(a)):
#     if a[i] - 1 != a[i-1]:
#           print(a[i-1] +1)



# Напишите программу, удаляющую из текста все слова содержащие "абв".

my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв"'
print(f'Изначальный вид текста: {my_text}')
def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)

# text = str('абвольт (абв) — единица измерения электрического потенциала (напряжения),\
# разности электрических потенциалов и электродвижущей силы (ЭДС) в СГСМ\
# (абсолютной электромагнитной системе сантиметр-грамм-секунда). 1 абвольт\
# равен 10–8 В. При разности потенциалов в 1 абвольт через сопротивление\
# 1 абом будет протекать ток силой 1 ампер. Для перемещения заряда величиной\
# в 1 абкулон между двумя точками с разностью потенциалов 1 вольт требуется\
# энергия в 1 эрг.')

# search_text = 'абв'
# print(f'Текст до обработки:\n{text}')
# print(f'\nУдалаяем из текста слова содержащие: \'{search_text}\'\n')
# lst = (" ".join([el for el in text.split() if search_text not in el]))
# print(f'Текст после обработки:\n{lst}\n\n'



