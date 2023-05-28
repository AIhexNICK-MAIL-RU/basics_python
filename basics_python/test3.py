def calculate(n, k): a = 1 
for i in range(1, n + 1): a *= i

b = 1
for i in range(1, k + 1): 
    b *= i
    
c = a // (b**n) 
p = int(c) 
q = 1
for i in range(1, c + 1): 
    if (p*q) % 1000000007 == c: 
        break
    q += 1

ans = (p * q - 1) % 1000000007
#return ans
n, k = map(int, input().split()) 
print(calculate(n, k))