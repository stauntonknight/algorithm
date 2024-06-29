from functools import cache

T = int(input())
for _ in range(T):
    n,m,k = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    vals = []
    for i, val in enumerate(a):
        vals.append((val, i))
    vals = sorted(vals)
    bought = [0] * len(vals)
    tc = 0
    for cost, index in vals:
        bought[index] = min(m, k)
        k = k - min(m, k) 
    curr = 0
    cost = 0
    for i in range(n):
        cost = cost + (curr + a[i]) * bought[i]
        curr = curr + bought[i]
    print(cost)



