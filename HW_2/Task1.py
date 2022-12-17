# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

# a = input()
# list_num = a.split('.')
# print(list_num)
# for i in range(len(list_num)):
#     list_num[i] = int(list_num[i])
# print(list_num)

s = list(map(int, (input().split('.'))))
sum = 0
for i in range(len(s)):
    x = s[i]
    while(x > 0):
        sum += (x % 10)
        x = x//10
print(sum)