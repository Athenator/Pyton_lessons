# реализуйте RLE алгоритм: модуль сжатия и восстановления данных

def encode(s):
    encoding = ""  
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1

    return encoding

s = input('Введите буквы, которые необходимо сократить: ')
print(encode(s))
