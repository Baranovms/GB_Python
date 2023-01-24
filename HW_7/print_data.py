def print_data(data):
    if len(data) > 0:
        print("ID".center(5), "Имя".center(20), "Фамилия".center(20), "Отчество".center(20), "Телефон".center(15), "Комментарий".center(50))
        print("-" * 130)
        for item in data:
            print(item[0].center(5), item[1].center(20), item[2].center(20), item[3].center(20),
                  item[4].center(15), item[5].center(50))
    else:
        print("Справочник пуст!")
