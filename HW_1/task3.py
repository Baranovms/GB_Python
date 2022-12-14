# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x, y = int(input()), int(input())
if x == 0 or y == 0:
    print('Точка лежит на осях координат')
if x > 0 and y > 0:
    print('I четверть')
if x < 0 and y > 0:
    print('II четверть')
if x < 0 and y < 0:
    print('III четверть')
if x > 0 and y < 0:
    print('IV четверть')