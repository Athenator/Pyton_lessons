#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Введите число: '))
str_num = str(num)
sum = 0
for i in range(len(str_num)):
    if str_num[i].isnumeric():
        sum += int(str_num[i])
    
print(f' - {num} -> {sum}')

