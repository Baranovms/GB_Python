from import_data import import_data
from export_data import export_data
from print_data import print_data
# from search_data import search_data

def greeting():
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    id = input('Введите ID: ')
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите комментарий: ")
    return [id, last_name, first_name, middle_name, brith_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("ID".center(5), "Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Комментарий".center(30))
            print("-"*140)
            print(item[0].center(5), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(20), item[5].center(15), item[6].center(30))
        else:
            print("Данные не обнаружены")