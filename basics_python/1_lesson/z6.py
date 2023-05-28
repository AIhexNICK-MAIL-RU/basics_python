# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали 
# билет с номером. Счастливым билетом называют такой 
# билет с шестизначным номером, где сумма первых трех 
# цифр равна сумме последних трех. Т.е. билет с номером 
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется 
# написать программу, которая проверяет счастливость билета.

# *Пример:
# 385916 -> yes
# 123456 -> no

# bilet = int(input())
# a = int(bilet / 100000)
# b = abs(int(a * 10 - bilet / 10000))
# c = int(bilet / 1000 - a * 100 - b * 10)
# bigHalf = bilet // 1000 * 1000
# half1 = int(a + b + c) 
# smallHalf = bilet - bigHalf
# d = smallHalf // 100
# e = abs(smallHalf // 10 - d * 10)
# f = smallHalf % 10
# half2 = d + e + f 
# if half1 == half2:
#     print('yes')
# else:
#     print('no')

bilet = input()
if len(bilet) == 6:
    x1 = int(bilet[:3])
    x2 = int(bilet[3:])
    sum1 = 0
    sum2 = 0
    while x1 != 0:
        sum1 += x1 % 10
        x1 //= 10
    while x2 != 0:
        sum2 += x2 % 10
        x2 //= 10
    if sum1 == sum2:
        print('yes')
    else:
        print('no')
else:
    print('это не билет')