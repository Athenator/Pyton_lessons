# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# Добавьте игру против бота
import random
sweets = 2021
while sweets > 0:
    input_error_player = True
    while input_error_player:
        a = input('Введите число конфет от 0 до 28: ')
        try:
            if int(a) > sweets:
                print(f'Введите число, меньше чем колличество оставшихся конфет')
                input_error_player = True
            elif int(a) <= 0 or int(a) > 28:
                    print('Введите число больше 0 и меньше 28!')
                    input_error_player = True
            else: 
                input_error_player = False
                print(f'Вы взяли - {a} конфет(ы)')
        except Exception:
            print('Вы ввели неккоректные данные, попробуйте снова!')
            input_error_player = True

    sweets -= int(a)
    if sweets == 0:
        print('Игра окончена, игрок выйграл.')
        input_error_bot = False
        break
    print(f'Конфет осталось {sweets}')
    input_error_bot = True
    while input_error_bot:
        if sweets < 28:
            b = random.randint(1,sweets)
            input_error_bot = False
            print(f'Бот взял - {b} конфет(ы)')
        else: 
            b = random.randint(1,28)
            input_error_bot = False
            print(f'Бот взял - {b} конфет(ы)')
        sweets -= b
        print(f'Конфет осталось {sweets}')
    if sweets == 0:
        print('Игра окончена, бот выйграл.')
        input_error_player = False
        break
    
    
            


            