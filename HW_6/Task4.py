# 4. Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

N = int(input('Введите количество членов последовательности: ')) #можно было и N запихнуть в print, но как говорили на лекции не рекомендуется нагромождать.
print([3**i if i % 2 == 0 else -3**i for i in range(N)])
