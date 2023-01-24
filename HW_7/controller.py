from import_base import import_base
from export_base import export_base
from print_data import print_data
from print_name import print_name


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
    2 - экспорт;\n\
    3 - экспорт имени и фамилии.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_base(input_data(), sep)
    elif ch == '2':
        data = export_base()
        print_data(data)
    else:
        data = export_base()
        print_name(data)
