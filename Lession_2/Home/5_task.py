# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]
fib_list = []
fib_reverse_list = []

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


num = int(input("Введите число: "))
print("Последовательность Нега Фибоначчи:")
for i in range(num + 1):
    fib_list.append(fibonacci(i))

f = -1
for i in range(num):
    if num % 2 == 0:     
        if i % 2 == 0:
            fib_reverse_list.append(-fib_list[f])
        else:
            fib_reverse_list.append(fib_list[f])
    else:
        if i % 2 != 0:
            fib_reverse_list.append(-fib_list[f])
        else:
            fib_reverse_list.append(fib_list[f])            
    f -= 1

print(fib_reverse_list + fib_list)
