# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from decimal import Decimal

# a = [1.1, 1.2, 3.1, 5, 10.01]
# b = []
# for i in a:
#     if i % 1 != 0:
#         b.append(Decimal(str(i%1))) 
# b.sort()

# print(f'Разницп между значениями : {b[len(b)-1]-b[0]}')


def make_list(array, count):
    array = []
    for i in range(count):
        num = float(input(f'Введите элемент списка № {i + 1} : '))
        if sol(num) == 0:
            num = int(num)
        array.append(num)
        
    return array


def sol(n):
    dec = divmod(n, 1)
    return round(list(dec)[1], 10)


size = int(input('Введите размер списка: '))
arrf = []
flist = make_list(arrf, size)


fmin = sol(flist[0])
fmax = sol(flist[0])
for i in range(size):
    if sol(flist[i]) != 0:
        if sol(flist[i]) > fmax:
            fmax = sol(flist[i])
        elif sol(flist[i]) < fmax and sol(flist[i]) < fmin:
            fmin = sol(flist[i])
print(f'Минимальный элемент - > {fmin}\nМаксимальный элемент -> {fmax}')


# num_min = sol(fmin)
# num_max = sol(fmax)

diff = fmax - fmin

print(flist, ' => ',round(diff, 10))
# lst = [1.1, 1.2, 3.1, 5, 10.01]

# lst = [round(val % 1, 2) for val in lst]
# rev_result = max(lst) - min(lst)
# print(max(lst), min(lst))
# print(rev_result)