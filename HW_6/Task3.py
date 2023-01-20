# 3. Найти произведение пар чисел списка (парой считаем первый и последний, второй предпоследний и тд)

lst = [2, 3, 4, 2, 5, 7, 8, 10]
multiply = [lst[i] * lst[len(lst)-1 -i] for i in range(len(lst)//2 + len(lst)%2)]
print(multiply)