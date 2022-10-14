# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


# Пример с неповторющимеся элементами последовательности:
#
# converted_list = list(map(int, '1 2 2 3 3 4 5'.split()))
# print('Изначальный список: {converted_list}')
#
# Тот же пример с  Lambda и Filter
#
# filter_list = list(filter(lambda x: converted_list.count(x) == 1, converted_list))
#
# Тот же пример с List comprehension
#
# filter_list = [x for x in converted_list if converted_list.count(x) == 1]
# print(f'Измененный список: {filter_list}')


#  Пример с использованием функции Enumerate

# lst = [12, 19, 22, 31, 52, 78]
# for id, el in enumerate(lst):
#     print(f'Индекс: {id}, элемент: {el} из списка: lst')

# lst = ['12', '19', '22', '31', '52', '78']
# lst = list(enumerate(lst))
# print(lst)

# Пример использования функции filter
# Проверка числа на четность

# lst = [10, 11, 20, 21, 30, 33]
#
# def filt_num(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# lst = list(filter(filt_num, lst))
# print(f'Все четные числа в списке: {lst}')


# Пример функции с лямбдой

# lam = lambda x, y: x + y
# print(lam(5, 10))

# Пример использования Map
lst_num = [10, 23, 34, 56, 87]
lst_float = list(map(float, lst_num))
print(lst_float)
