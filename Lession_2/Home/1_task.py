# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

arrn = input('Задайте список из чисел: ' )
sum_list = 0
# for i in len(List):
#     if i % 2 != 0:
#         sum_list += int(List[i])

# num = input()
# for i in range(1,num+1):
#     List.append(i)
arr = []

for i in range(len(arrn)):
    arr.append(int(arrn[i]))
    if i % 2 != 0:
         sum_list += int(arrn[i])
    

print(f'{arr} -> Сумма элементов на нечетных позициях: {sum_list}')