from primesieve import primes

p = primes(1000000)

def fi(n):
    res = n
    i = 0
    while p[i] * p[i] <= n:
        if n % p[i] == 0:
            res = res * (1 - 1 / p[i])
            while n % p[i] == 0:
                n = n // p[i]
        i += 1
    if n != 1:
        res = res * (1 - 1 / n)
    return res

count = 0
for i in range(1, 1000001):
    count += fi(i)
print(count)
