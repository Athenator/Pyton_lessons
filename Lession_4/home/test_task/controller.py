import in_out
import ui


def button_click():
    ui.print_data('Введите: \n1. Для просмотра полного справочника.\n2. Для добавления данных в справочник\n'
                  '3. Для экспорта справочника\n4. Для активации поиска.')
    user_answer = ui.input_data()
    if user_answer == '1':
        list_data = in_out.get_info('Sprav.txt')
        ui.print_all(list_data)
    elif user_answer == '2':
        in_out.append_data('Sprav.txt', ui.add_data())
        print('Вы успешно записали данные в справочник!')
    elif user_answer == '3':
        print('Выберите формат, в которые вы хотите экспортировать данные:\n1. Txt\n2. Csv')
        expo = ui.input_data()
        if expo == '1':
            in_out.export_txt(in_out.get_info('Sprav.txt'))
            print(f'Вы успешно экспортировали справочник в свой фаил под названием: Export.txt')
        if expo == '2':
            in_out.export_csv(in_out.get_info('Sprav.txt'))
            print(f'Вы успешно экспортировали справочник в свой фаил под названием: Export.csv')
    elif user_answer == '4':
        print('Введите номер ID человека, чей номер вы хотите узнать')
        in_out.search_str()

