# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#Вариант 1
# num = int(input())
# print(f'{num} -> {bin(num)[2:]}')

#Вариант 2
s = ''
num = int(input())
while (num != 0):
    s += str(num % 2)
    num //= 2
print(s)
