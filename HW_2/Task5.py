# Реализуйте алгоритм перемешивания списка.

from random import *

N = int(input('Задайте количество элеметнов списка: '))
s = []
for i in range(N):
    s.append(randint(-N, N + 1))
print(f'Сгенерированный список: {s}')
new_s = s[:]
for i in range(len(new_s)):
    index = randint(0, len(new_s)-1)
    temp = new_s[i]
    new_s[i] = s[index]
    new_s[index] = temp
print(f'Рандомный список: {new_s}')