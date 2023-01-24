# Домашние задания по Python

## В папке HW_1 добавлены решения задач к дз 1
1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:
        
        * 6 -> да
        * 7 -> да
        * 1 -> нет
2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:
    
         * x=34; y=-30 -> 4
         * x=2; y=4-> 1
         * x=-34; y=-30 -> 3
3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

        * A (3,6); B (2,1) -> 5,09
        * A (7,-5); B (1,-1) -> 7,21

## В папке HW_2 добавлены решения задач к дз 2

1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

        * 6782 -> 23
        * 0,56 -> 11
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

        * пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

Пример:

        * Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
        * Сумма 9.06
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
5. Реализуйте алгоритм перемешивания списка.

## В папке HW_3 добавлены решения задач к дз 3

1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

## В папке HW_4 добавлены решения задач к дз 4

1. Вычислить число c заданной точностью d

   Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

   Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


## В папке HW_5 добавлены решения задач к дз 5

Обязательная:
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

Далее заадчи на выбор:

2(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 

В качестве дополнительного усложнения можно:
        a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
        b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )

2(2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

Обязательная:
3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Модуль сжатия:
Для чисел:
Входные данные:
111112222334445
Выходные данные:
5142233415
Также должно работать и для букв:
Входные данные:
AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
Выходные данные:
6A1F2D7C1A17E
(5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

## В папке HW_6 добавлены решения задач к дз 6
- С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
1. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

A (3,6); B (2,1) -> 5,09
A (7,-5); B (1,-1) -> 7,21
2. Найти сумму чисел списка стоящих на нечетной позиции
3. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
4. Сформировать список из N членов последовательности
Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

## В папке HW_7 добавлены решения задач к дз 7

Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
Модуль контроллер
Модуль для импорта(ввода данных)
Модуль для экспорта(вывод данных)
Строка содержит id,имя,фамилию,номер телефона, комментрий - символ разделитель на выбор(можно использовать пробел или запятые) + файл с хранением этих строк
*Добавить сортировку по имени или по id
*Добавить вывод только имени и фамилии