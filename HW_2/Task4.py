# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import *

N = int(input('Задайте количество элеметнов списка: '))
s = []
for i in range(N):
    s.append(randint(-N, N + 1))
print(f'Сгенерированный список: {s}')


product = 1
f = open('File.txt','r')
list = f.readlines()
list = [line.rstrip() for line in list]
for i in list:
    product *= s[int(i)]
f.close()
print(f'Произведение элементов {list} равно: {product}')

