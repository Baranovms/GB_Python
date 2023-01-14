text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {text}")
n = "абв"
res = [i for i in text.split() if n not in i]
print(f'Результат: {" ".join(res)}')


# Решение от преподавателя на семинаре
# text = "ааабваа! аааа, аабв вввв. Абв ггг"
# text_list = text.split()
# result = list(filter(lambda x: not "абв" in x.lower() ,text_list))
# print(result)