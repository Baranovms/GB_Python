# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# # Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.


def encode(text):
    count = 1
    result = ''
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        result = result + str(count) + text[-1]
    return result

def recovery(code):
    number = ''
    result = ''
    for i in range(len(code)):
        if not code[i].isalpha():
            number += code[i]
        else:
            result = result + code[i] * int(number)
            number = ''
    return result


message = input('Введите строку для преобразования: ')
print(f'Текст после кодировки: {encode(message)}')
print(f'Текст после дешифровки: {recovery(encode(message))}')