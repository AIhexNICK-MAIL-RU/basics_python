# Последовательностью Фибоначчи называется 
# последовательность чисел a0, a1, ..., an, ..., 
# где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21

def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input('Введите номер элемента: '))
list_f = []
for i in range(3, n):
    list_f.append(fib(i - 2))
print(list_f)