list1 = [1,2,3,4,5]
list2 = list1

list1[0] = 10
list2[1] = 10
# print(list1)
# print(list1.pop(2))
# print(list1)

print(list1.insert(2,11))
print(list1)

exit()
a = {5,6,1,2,7}
b = {11, 22, 33, 44, 55}
c = a.copy()
u = a.union(b)

colors = {'red','blue','white'}
colors.add('grey')
print(f'Добавили grey = {colors}')
colors.remove('red')
print(f'Удалили red = {colors}')
colors.clear()
print(f'очистили множество = {colors}')
dict = {}

dict = \
    {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4
    }

print(dict['two'])
for i in dict.keys():
#for i in dict:
    #print(dict[i])
    print(i)
t = tuple(['red', 'green', 'blue'])
red, green, blue = t 
print('r: {} g: {} b: {}' .format(red,green,blue))
a = (3, 4,2,6)

for i in a:
    print(i)
def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib (n - 1) + fib(n - 2)

list = []
for e in range(1,10):
    list.append(fib(e))
print(list)
def concat (*params) :
    res: str = ''
    #res: int = 0
    for item in params:
        res += item 
    return res
    
print(concat('a', 'b', 'c', 'd', 'w'))
print(concat('a', '1'))
#print(concat(1,2,3,4))


import zeus
print(zeus.G(3))
print(zeus.G('a'))

import Athena as h

print (h.f(2.3))


path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


with open('file.txt', 'w') as data:
    data.write('line 12 \n')
    data.write('line 21 \n')

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
# data.writelines(colors)
data.write('Line 2\n')
data.write('line 3\n')
data.close()
