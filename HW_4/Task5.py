# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

file1 = open('zadanie5_1.txt', 'r')
file2 = open('zadanie5_2.txt', 'r')
file3 = open('zadanie5_summa.txt', 'w')

f1 = file1.readline()
lst_f1 = f1.split()
print(lst_f1, type(f1))
# dict_f1 = {}
# for i in range(len(lst_f1)):
#     dict_f1[i] = lst_f1[i]
# print(dict_f1, type(f1))

f2 = file2.readline()
lst_f2 = f2.split()
print(lst_f2, type(f2))
# dict_f2 = {}
# for i in range(len(lst_f2)):
#     dict_f2[i] = lst_f2[i]
# print(dict_f2, type(f2))
for i in range(len(lst_f1)):
    if lst_f1[i] != lst_f2[i]:
        file3.write(f'{str(int(lst_f1[i])+int(lst_f2[i]))} ')
    else:
        file3.write(f'{lst_f1[i]} ')

file1.close
file2.close
file3.close