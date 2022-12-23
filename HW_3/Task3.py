# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = []
for i in range(len(lst)):
    if lst[i] % 1 !=0:
        new_lst.append(lst[i])
res_lst = []
for i in range(len(new_lst)):
    res_lst.append(round(new_lst[i] % 1, 2))
print(f'{res_lst} => {max(res_lst) - min(res_lst)}')