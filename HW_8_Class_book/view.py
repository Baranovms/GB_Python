def menu():
    pos_menu = int(input(" 1 - добавить ученика, \n 2 - добавить предмет,\n 3 - добавить оценку,\n 4 - показать весь список учеников,\n 5 - показать выбранного ученика, \n 6 - выход\n"))
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