n, k = map(int, input().split())

# функция для нахождения количества делителей числа


def num_divisors(num):


res = 1
i = 2
while i*i <= num:
cnt = 0
while num % i == 0:
cnt += 1
num //= i
res *= cnt + 1
i += 1
if num > 1:
res *= 2
return res

функция для вычисления вероятности победы первого игрока


def calc_prob(n, k):


    # создаем массив all_divisors[i][j], где all_divisors[i][j] содержит все числа,
    # которые можно получить при броске i кубиков с гранями от 1 до j включительно
all_divisors = [[set() for j in range(k)] for i in range(n+1)]
for j in range(1, k+1):
all_divisors[1][j-1].add(j)
for i in range(2, n+1):
for j in range(1, k+1):
for div in all_divisors[i-1][j-1]:
all_divisors[i][j-1].add(div*j)
# вычисляем вероятность победы первого игрока
num_win = 0
total = kn
for i in range(1, n+1):
for j in range(k):
for num in all_divisors[i][j]:
if num == 1:
continue
if num_divisors(num) % 2 == 1:
if (n-i) % 2 == 1:
num_win += ki
else:
num_win -= k**i
return num_win / total

# вычисляем вероятность победы первого игрока
prob = calc_prob(n, k)

# находим несократимую дробь p/q, остаток p*q_inv mod 10^9+7 и выводим его
p, q = prob.as_integer_ratio()
q_inv = pow(q, -1, 1000000007)
res = (p * q_inv) % 1000000007
print(res)
