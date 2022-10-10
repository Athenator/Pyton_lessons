# def f(x):
#     return x**2


# g = f
# print(g(1))
# Можно называть функцию переменной


# def calc1(x):
#     return x + 10


# def calc2(x):
#     return x * 10


# def math(op, x):
#     print(op(x))

# def sum(x,y):
#     return x + y
# То же самое что и с верху

# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))
#     return op(a,b)

# calc(lambda x, y: x + y, 5, 5) Вызов функции при помощи лямбды
# math(calc1,10)
# Вызов функции в функции
# def f (x):
#     return x ** 2

# list = [(i,f(i)) for i in range(1,39) if i % 2 == 0]
# list = [(i,f(i)) for i in range(1,6)]
# Сокращение ^ того, что ниже
# for i in range(1,101):
#     list.append(i)


# path = 'file.txt'
# f = (open(path, 'r'))
# data = f.read() + ' '
# f.close()
# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e ** 2))

# print(out)

#  Чтение и работа с файлом ^

# def select(f,col):
#     return [f(x) for x in col]
# Функция map в алгоритме ^

# def where(f,col):
#     return [x for x in col if(x)]
# Функция filter в aлгоритме ^

# data = '2  8  38'.split()

# res = list(map(int, data))
# res = list(filter(lambda x: not x % 2, res))
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

#  Та же задача,что выше.

# li = [x for x in range(1, 20)]
# li = list(map(lambda x:x + 10, li))
# print(li)

# Функция Map ^

# data = list(map(int,'1 2 3 45'.split()))

# for e in data:
#     print(e)
# print('--')
# for e in data:
#     print(e)

#  Ещё Map

# data = [x for x in range(10)]

# res = list(filter(lambda x: x % 2 != 0, data))
# print(res)

# Работа метода filter

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14]
sala = [11, 22, 33]
# data = list(zip(users, ids, sala))
# Работа Zip
data = list(enumerate(users))
# Работа enumerate
print(data)

