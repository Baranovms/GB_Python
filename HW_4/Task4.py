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

file.write(f'{x} \n')
file.close()

# import random
# k = int(input())
# result = ""
# for i in range(k,-1,-1):
#     koef = random.randint(0,3)
#     if koef == 0:
#         continue
#     if i == 1:
#         if koef>1:
#             result+=f"{koef}*x+"
#         if koef == 1:
#             result+= f"x+"
#     if i > 1:
#         if koef > 1:
#             result += f"{koef}*x**{i}+"
#         if koef == 1:
#             result += f"x**{i}+"
#     if i == 0:
#         if koef > 1:
#             result += f"{koef}+"
#         if koef == 1:
#             result += f"1+"
# print(result[:-1]+" = 0")


# import random
# k = int(input('Введите натуральную степень k: '))
# coef_list = [random.randint(0,100) for i in range(k+1)]
# print(coef_list)
# path = 'polynomial.txt'
# with open(path, 'w') as data:
#     for i in range(k, -1, -1):
#         if coef_list[i] == 0:
#             continue
#         data.write(str(coef_list[i]) + ('*x' if i!=0 else ''))
#         data.write(('**'+str(i)) if i > 1 else '')
#         data.write('+' if i!=0 else '')
#     data.write('=0')
