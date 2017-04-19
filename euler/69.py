from sympy import isprime

def __gcd(x,y):
    if x == 0:
        return y
    if x > y:
        return __gcd(y,x)
    return __gcd(y%x, x)

def is_coprime(x, y):
    return __gcd(x,y) == 1

def get_f(n):
    f = []
    i = 2
    while i*i <= n:
        if n % i == 0 and isprime(i):
            f.append(i)
            while n % i == 0:
                n = n / i
        if i == 2 :
            i += 1
        else:
            i += 2
    if n != 1:
        f.append(n)
    return f

max_num = 1000000
found = False
maxim = 0

for i in range(2, max_num + 1):
    factors = get_f(i)
    s = set(range(1, i+1))
    for num in s.copy():
        for f in factors:
            if num % f == 0:
                s.discard(num)
                break
    n_cp = len(s) 
    if not found or maxim < i / n_cp:
        maxim = i/n_cp
        found = True

print(maxim)
