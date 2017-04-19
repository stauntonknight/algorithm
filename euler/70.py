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

found = False
max = 0
val = 0
for i in range(2, 10000001):
    ans = int(fi(i))
    if ''.join(sorted(str(ans))) == ''.join(sorted(str(i))):
        print (i)
        if not found or max >  i / ans:
            found = True
            max = i / ans
            val = i

print(max)
print(val)


