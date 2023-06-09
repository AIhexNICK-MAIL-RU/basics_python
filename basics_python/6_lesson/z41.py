# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

from random import randint

def genList1(n):
    a = []
    for i in range(n):
        a.append(randint(1, 9))
    return a

one = genList1(int(input('введите к-во эл-в в массиве: ')))

print('Первый массив: ')
print(one)

new = []
for i in range(1, len(one) - 1):
    if one[i + 1] < one[i] > one[i - 1]:
        new.append(one[i])

print(new)
print('Результат')
print(len(new))