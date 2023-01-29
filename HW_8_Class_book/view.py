def menu():
    pos_menu = int(input("\
    1 - Добавление нового студента\n\
    2 - Добавление предмета\n\
    3 - Добавление оценки ученику по предмету\n\
    4 - Показ списка учеников\n\
    5 - Показ листа оценок конкретного ученика\n\
    6 - Выход из программы\n\
    Ваш выбор: "))
    return pos_menu

def add_student():
    student = input("Введите Имя и Фамилию: ")
    return student

def add_discipline():
    discipline = input("Введите предмет: ")
    return discipline

def get_assessment():
    student = input("Введите Имя и Фамилию: ")
    discipline = input("Введите предмет: ")
    assessment = input("Введите оценку по предмету: ")
    return student, discipline, assessment

def search_statement_student():
    student = input("Введите Имя и Фамилию ученика для просмотра оценок:")
    return student