# 1. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from functools import reduce
coord_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split()))
coord_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def distance(coord_1, coord_2):
     dist = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(coord_1, coord_2))))
     return round(dist, 2)
print(distance(coord_1, coord_2))