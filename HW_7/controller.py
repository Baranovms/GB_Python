from import_base import import_base
from export_base import export_base
from print_data import print_data


def greeting():
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    id = input('Введите ID: ')
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    surname = input("Введите отчество: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите комментарий: ")
    return [id, last_name, first_name, surname, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_base(input_data(), sep)
    else:
        data = export_base()
        print_data(data)
