from math import factorial

def ncr(n, r):
    return factorial(n)/factorial(r)/factorial(n-r)

c = 0
for i in range(23, 101):
    for j in range(1, i):
        num = ncr(i,j)
        if num > 1000000:
            c = c+1

