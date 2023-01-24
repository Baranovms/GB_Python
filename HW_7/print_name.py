def print_name(data):
    if len(data) > 0:
        print("Имя".center(20), "Фамилия".center(20))
        print("-" * 40)
        for item in data:
            print(item[1].center(20), item[2].center(20))