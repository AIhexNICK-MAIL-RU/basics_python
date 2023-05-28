# Задача No35. Общее обсуждение
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

def prost(x, z = 2):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % z == 0:
        return False
    elif z * z > x:
        return True
    else:
        return prost(x, z + 1)
    
x = int(input())
print(prost(x))