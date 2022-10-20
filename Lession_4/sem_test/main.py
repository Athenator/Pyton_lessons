import controller


flag = False
while flag == False:
    try:
        controller.button_click()
    except ValueError:
        print('Вы ввели неккоретные данные')
        flag = True
