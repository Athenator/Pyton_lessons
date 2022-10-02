# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o [2, 3, 4, 5, 6] => [12, 15, 16];
# o [2, 3, 5, 6] => [12, 15]

arrn = input('Зайдайте список из чисел: ')
arr = []
count = len(arrn) // 2
rever_i = 0
for i in range(count):
    rever_i -= 1
    arr.append(int(arrn[i]) * int(arrn[rever_i]))
    
if len(arrn) % 2 != 0:
    arr.append(int(arrn[count]) * int(arrn[count]) )

arre = []
for i in range(len(arrn)):
    arre.append(int(arrn[i]))

print(f'{arre} => {arr}')
