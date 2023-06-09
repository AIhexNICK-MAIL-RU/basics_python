# Задача 26 (дз):  Напишите программу, которая на вход 
# принимает два числа A и B, и возводит число А в 
# целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def rec_rate(a, b):
    if b == 0:
        return 1
    return a * rec_rate(a, b - 1)

a = int(input('введите а: '))
b = int(input('введите b: '))
print(rec_rate(a, b))