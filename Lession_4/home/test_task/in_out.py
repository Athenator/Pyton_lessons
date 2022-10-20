def append_data(name_file, data):
    with open(name_file, 'a', encoding='utf-8') as file:
        file.write(f"\n{data},")


def get_info(name_file):
    with open(name_file, 'r', encoding='utf-8') as file:
        info = file.read().split(",")
    return info

def search_str():
    num = input("id: ")
    with open("Sprav.txt", 'r', encoding='utf_8') as f:
        lst = f.readlines()

    for i in lst:
        if f'id {num}' in i:
            print(i)

def export_txt(data):
    with open('Export.txt', 'a', encoding='utf-8') as file:
        for i in get_info('Sprav.txt'): file.write(f"{i},")

def export_csv(data):
    with open('Export.csv', 'a', encoding='utf-8') as file:
        for i in get_info('Sprav.txt'): file.write(f"{i},")