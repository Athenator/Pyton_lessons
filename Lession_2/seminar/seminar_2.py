# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# number = int(input('Input the number: '))
# d = {i : 3*i + 1 for i in range(1,number+1)}
# print(f"Dictonary: {d}")
# # print(d[5])
# d = {'one': None}
# d['one'] = 5
# d['twho'] = 6
# d.update(three = '7', four = 8)
# d.setdefault('five', 9)
# d.update({'ten' : 3})
# print(d)

# n = int(input('N = '))
# d = {}
# for i in range(1, n+1):
#     d[i] = 3*i + 1
# print(d)

# print(eval('2+2'))

# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельз

# lst = [1, 5, 2, 3, 4, 6, 1, 7]
# lst = list(map(int,lst))

# for i in range(len(lst)):
#     lst_1 = []
#     lst_1.append(lst[i])
#     for j in range(i, len(lst)):
#         if lst_1[-1] < lst[j]:   
#             lst_1.append(lst[j])

#     print(lst_1)


# Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. Приоритет оперции стандартный. Пример 2 + 2 => 4;1 + 2 * 3 => 7

st = input('ведите математическое выражение: ')
for el in ['+', '-', '*', '/']:
    st = st.replace(el, f' {el} ')
st_list = st.split()

for i in range(len(st_list)-1):
    if st_list[i] == '*':
        result = int(st_list[i-1]) * int(st_list[i+1])
        st_list[i] = result
        st_list[i-1] = None
        st_list[i+1] = None
st_list = [el for el in st_list if el != None]

print(st_list)