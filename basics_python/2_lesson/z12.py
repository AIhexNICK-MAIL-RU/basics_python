# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

# s = int(input())
# p = int(input())
# d = s ** 2 - 4 * p
# if d > 0:
#     y1 = float((s + d ** 0.5) / 2)
#     y2 = float((s - d ** 0.5) / 2)
#     x1 = s - y1
#     x2 = s - y2
# elif d < 0:
#     y1 = y2 = s / 2
#     x1 = x2 = s - y1
# else:
#     print('no roots')
# print(x1, x2, y1, y2)

# s = int(input('Введите сумму чисел: '))
# p = int(input('Введите произведение чисел: '))
# for i in range(s):
#     for j in range(s):
#         if s == i + j and p == i * j:
#             x = i
#             y = j
# print (f"x = {x}, y = {y} или x = {y}, y = {x}")

x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)