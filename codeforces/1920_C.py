import math
T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    a = list(map(int, input().split()))
    for i in range(1, N + 1):
        if N % i == 0:
            g = 0
            for j in range(i):
                for k in range(j + i, N, i):
                    g = math.gcd(g, abs(a[k] - a[k - i]))
            if g != 1:
                ans += 1
                # print(i, g)
            # else:
                # print("No", i)
    print(ans)  