# Напишите программу, которая принимает на вход координаты точки х и Y). 
# причем х * О и Y о и выдает номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

ax = int(input())
ay = int(input())
if ax > 0 and ay > 0:
    print(1)
elif ax < 0 and ay > 0:
    print(2)
elif ax < 0 and ay < 0:
    print(3)
elif ax > 0 and ay < 0:
    print(4)
else:
    print('на оси')
    