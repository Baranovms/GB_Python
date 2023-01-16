# 2(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
#
# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )


from random import randint
# работает для решения игры в двух режимах (игрок-игрок и игрок-бот). не реализовал интеллект, может быть чуть больше времени и все сделал бы.

def players(konf):
    while konf >= 0:
        player_1 = int(input('Сколько конфет возьмешь? '))
        if player_1 > 28 or player_1 > konf:
            print('Столько брать нельзя, начни сначала')
            break
        else:
            konf -= player_1
            if konf == 0:
                print('Поздравляю! Вы выиграли!')
                break
            if konf >= 28:
                print(f'Осталось конфет: {konf}')
                player_2 = int(input('Второй игрок берет конфет: '))
                if player_2 > 28 or player_2 > konf:
                    print('Столько брать нельзя, начнем сначала')
                    break
                else:
                    konf -= player_2
                    print(f'Осталось конфет: {konf}')
            elif konf <= 28:
                print(f'Осталось конфет: {konf}')
                player_2 = int(input('Второй игрок берет конфет: '))
                if player_2 > 28 or player_2 > konf:
                    print('Столько брать нельзя, начнем сначала')
                    break
                else:
                    konf -= player_2
                    print(f'Осталось конфет: {konf}')
            if konf == 0:
                print('Вы проиграли!')
                break
def bot(konf):
    while konf >= 0:
        man = int(input('Сколько конфет возьмешь? '))
        if man > 28 or man > konf:
            print('Столько брать нельзя, начни сначала')
            break
        else:
            konf -= man
            if konf == 0:
                print('Поздравляю! Вы выиграли!')
                break
            if konf >= 28:
                bot = randint(1, 29)
                print(f'Бот взял конфет: {bot}')
                konf -= bot
                print(f'Осталось конфет: {konf}')
            elif konf <= 28:
                bot = randint(1, konf)
                print(f'Бот взял конфет: {bot} ')
                konf -= bot
                print(f'Осталось конфет: {konf}')
            if konf == 0:
                print('Вы проиграли!')
                break





print('Игра "Конфеты".За раз вы можете взять не более 28 конфет,')
print('выигрывает тот, кто возьмет последнюю конфету')

konf = int(input('Введите количество конфет в вазе: '))
if konf < 29:
    print('Недостаточно конфет. Начни сначала')
else:
    print('Выберите против кого играете:')
    vs = input('1 - Игрок\n2 - Бот\nВаш выбор: ')

    if vs == '1':
        players(konf)
    else:
        bot(konf)



