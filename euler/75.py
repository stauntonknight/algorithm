import math

N = 1500000
m = 2
a = 0
b = 0
c = 0
p = a + b + c
total_k = {}
while m <= math.sqrt(N/2):
    n = 1
    while n < m:
        a = m * m - n * n
        b = m * n * 2
        if a > b:
            x = a
            a = b
            b = x
        c = m * m + n * n
        t = 1
        p = a + b + c
        while t * p <= N :
            if t * p not in total_k:
                total_k[t * p] = []
            total_k[t * p].append((t * a, t * b, t * c))
            t += 1
        n += 1
    m += 1

kount = 0
a_kount = 0
for a in total_k:
    total_k[a] = set(total_k[a])
    if len(total_k[a]) == 1:
        kount += 1
    else:
        a_kount += 1

print(kount)
print(a_kount)
    

