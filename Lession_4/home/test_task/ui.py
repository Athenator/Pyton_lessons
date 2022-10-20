import in_out
def print_all(data):
    for i in data: print(i)


def print_data(text=''):
    print(f"{text}")


def input_data(text=''):
    return input(f"Введите значение: {text}")


def add_data():
    id = input("Введите id: ")
    surname = input('Введите Фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    return f'id {id} {name} {surname} +7 {phone}'

def search_data():
    id_pes = input("id ")
    list_data = in_out.get_info("Sprav.txt")
    for i in list_data:
        if f"id {id_pes}" in i:
            print(i)

