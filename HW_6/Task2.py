# 2. Найти сумму чисел списка стоящих на нечетной позиции

my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(sum(my_list[1::2]))