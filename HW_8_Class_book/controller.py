import view

base = {}
students = []
disciplines = []

def start():
    while True:

        pos_menu = view.menu()
        if pos_menu == 1:
            student = view.add_student()
            if student not in students:
                students.append(student)
                base[student] = {}
        if pos_menu == 2:
            discipline = view.add_discipline()
            if discipline not in disciplines:
                disciplines.append(discipline)
                for student in students:
                    base[student][discipline] = []
        if pos_menu == 3:
            student, discipline, assessment = view.get_assessment()
            if discipline not in disciplines or student not in students:
                print('Not Found.\n Repeat, please')
            else:
                base[student][discipline].append(assessment)
        if pos_menu == 4:
            print(base)
        if pos_menu == 5:
            student = view.search_statement_student()
            print(base[student])
        if pos_menu == 6:
            break
        print('*' * 50)
        print(base)
        print('*' * 50)