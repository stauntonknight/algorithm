from functools import cache
from collections import deque
n,m = list(map(int, input().split()))
knt = 0
while True:
    if m <= n:
        print(knt + n - m)
        break
    if m & 1:
        m = m + 1
        knt += 1
    else:
        m = m // 2
        knt += 1