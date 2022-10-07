# Вычислить число π c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# import math
# from tkinter import N
# d = int(input('Введите точность числа π: '))
# p = math.pi

# def floor_float(variable: float, precision: d) -> str :
#     decimal_part = str(variable).split(".")[1]
#     if len(decimal_part) <= precision:
#         return str(variable)
#     else:
#         return str(round(variable, precision + 1))[:-1]

# n = floor_float(p,d)
# print (n)


# Другой способ

from time import process_time_ns


k = 1
my_pi = 0
d = input('d = ')

for i in range(1000000):
    if i % 2 == 0:
        my_pi += 4 / k
    else:
        my_pi -= 4 / k
    k += 2
process_time_ns
print(f'Число π c сточностью {d} : {str(my_pi)[:len(d)]}')