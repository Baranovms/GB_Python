#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#вариант 1
# from random import randint
#
# N = int(input())
# lst = []
#
# for i in range(1, N+1):
#     a = randint(-N, N+1)
#     lst.append(a)
# print(lst)
# print(set(lst))

#Вариант 2
from random import randint
def Random_list(N):
    for i in range(1, N+1):
        a = randint(-N, N+1)
        lst.append(a)
    return lst
def Search_Double(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

lst = []
N = int(input('Введите количество элементов последовательности: '))
print(Random_list(N))
lst = sorted(lst)
print(Search_Double(lst))

