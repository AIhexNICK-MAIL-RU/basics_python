#факториал и палиндром
def fuck (n, i = 1):
    if i < k:
        return fuck (i * n, i + 1)
    else:
        return(n)
    
# def fuck(n):
#     if n == 0:
#         return 1
#     return n * fuck(n - 1)

k = int(input('введите число: '))
print(fuck(k)) 

