from primesieve import primes

p = primes(1000000)
index = 0
ans = 1
while ans * p[index] <= 1000000:
    ans = ans * p[index]
    index = index + 1
print(ans)
