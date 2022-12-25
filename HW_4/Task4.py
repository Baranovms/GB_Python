# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
#    Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import *


file = open("zadanie4.txt", "w")
k = int(input("Введите число:   "))
lst = [randint(0, 100) for i in range(k + 1)]
print(lst)
x = ""
for i in range(k + 1):
    if i < k:
        x += str(lst[i]) + " * (x**" + str(k-i)  +  ") + "
    else:
        x += str(lst[i])
print(f'{x} = 0')

file.write(f'{x} = 0  \n')
file.close()