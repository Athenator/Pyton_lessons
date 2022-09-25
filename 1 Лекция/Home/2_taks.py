# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = input('Введите X: ')
y = input('Введите Y: ')
z = input('Введите Z: ')

xyz = [x, y, z]

print(xyz)

firstStatement = not (xyz[0] or xyz[1] or xyz[2])
secondStatement = not xyz[0] and not xyz[1] and not xyz[2]
result = firstStatement == secondStatement

if result == True:
    print('Утверждение верно!')
else:
    print('Утверждение не верно!')
