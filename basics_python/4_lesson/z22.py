# Задача 22: Даны два неупорядоченных набора целых 
# чисел (может быть, с повторениями). Выдать без 
# повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов 
# первого множества. m — кол-во элементов второго 
# множества. Затем пользователь вводит сами элементы 
# множеств.

import random
list1 = []
list2 = []
n = int(input())
m = int(input())

print('Введите элементы первого множества')
for i in range(n):
    list1.append(int(input(f'[{i}] = ')))

print('Введите элементы второго множества')
for i in range(m):
    list2.append(int(input(f'[{i}] = ')))

bunch = set()
for i in list1:
    if i in list2:
        bunch.add(i)
print('Конечное множество: ' + ', '.join(str(i) for i in sorted(bunch)))



# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')