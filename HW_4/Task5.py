# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

file1 = open('zadanie5_1.txt', 'r')
file2 = open('zadanie5_2.txt', 'r')
file3 = open('zadanie5_summa.txt', 'w')

f1 = file1.readline()
lst_f1 = f1.split()
print(lst_f1, type(f1))

f2 = file2.readline()
lst_f2 = f2.split()
print(lst_f2, type(f2))

for i in range(2, len(lst_f1)):
    if lst_f1[i] != lst_f2[i]:
        file3.write(f'{str(int(lst_f1[i])+int(lst_f2[i]))} ')
    else:
        file3.write(f'{lst_f1[i]} ')

file1.close
file2.close
file3.close



# #34. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
#
# pol1 = "2*x**10+3*x**9+2*x**8+3*x**7+1*x**6+2*x**5+3*x**4+3"
# pol2 = "6*x**13+3*x**10+2*x**7+1*x**6+2*x**2+3*x**1+10"
# print(pol1)
# print(pol2)
# pol1 = pol1.split("+")
# pol2 = pol2.split("+")
# print(pol1)
# print(pol2)
#
# result_pol = pol1 + pol2
# print(result_pol)
#
# polyn_dict = {}
#
# for value in result_pol:
#     if len(value)>1:
#         if value[1] in polyn_dict.keys():
#             polyn_dict[value[1]]+=value[0]
#         else:
#             polyn_dict[value[1]] = value[0]
#     else:
#         if 0 in polyn_dict.keys():
#             polyn_dict[0]+=value[0]
#         else:
#             polyn_dict[0] = value[0]
# print(polyn_dict)
# result_pol = dict(sorted(polyn_dict.items(),reverse=True))
# print(result_pol)
# finish_line = ""
# for stepen,koeff in result_pol.items():
#     if stepen>1:
#         finish_line+=f"{koeff}*x**{stepen}+"
#     if stepen == 0:
#         finish_line += f"{koeff}"
#
# print(finish_line)
