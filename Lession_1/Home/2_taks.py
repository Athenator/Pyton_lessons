# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = input('Введите X: ')
y = input('Введите Y: ')
z = input('Введите Z: ')


first_statement = not (x or y or z)
second_statement = not x and not y and not z
result = first_statement == second_statement

if result:
    print('Утверждение верно!')
else:
    print('Утверждение не верно!')