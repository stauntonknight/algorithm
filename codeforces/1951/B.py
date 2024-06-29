T = int(input())

for _ in range(T):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    k = k - 1
    our = a[k]
    best = n
    nxt = -1
    for i in range(n):
        if a[i] > a[k]:
            nxt = i
            break
    if nxt == -1:
        print(n - 1)
        continue

    positions = [0, nxt]
    best = -1
    for p in positions:
        a[k],a[p] = a[p], a[k]
        ans = 0
        block = False
        for i in range(p):
            if a[i] > a[p]:
                block = True
                break
        if block:
            best = max(best, ans)
            continue
        if p > 0:
            ans += 1
        for i in range(p + 1, n):
            if a[i] > a[p]:
                break
            ans += 1
        best = max(best, ans)
        a[k],a[p] = a[p], a[k]
    print(best)