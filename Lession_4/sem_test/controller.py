from operation import  summa, new_diff, multiplication, division
import Ui
import databse
import logger

def button_click():
    a = Ui.input_data('Введите а = ')
    b = Ui.input_data('Введите b = ')
    sign = Ui.input_data('Введите знак операции: ')
    databse.init(a, b)
    match sign:
        case '+': result = summa(databse.x, databse.y)
        case '-': result = new_diff(databse.x, databse.y)
        case '*': result = multiplication(databse.x, databse.y)
        case '/': result = division(databse.x, databse.y)
    Ui.print_data(result)
    logger.result_loger(f'{databse.x} {sign} {databse.y} = {result}')

