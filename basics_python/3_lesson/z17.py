# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# n = int(input[1, 1, 2, 0, -1, 3, 4, 4]) # неправильное мое решение
# k = int()
# for i in n:
#     if n[i] == n[i + 1]:
#         k += 1
#     i += 1
# print(k)

# n = [1, 1, 2, 0, -1, 3, 4, 4] #правильное чужое решение
# n = set(n)
# print(len(n))

list_1 = [1, 1, 2, 2, 3, 3, 4, 4]
result_list = list()
for i in list_1:
    if i not in result_list:
        result_list.append(i)
print(result_list)
print(len(result_list))