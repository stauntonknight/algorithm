T=int(input())

for _ in range(T):
    n = int(input())
    s = input()
    done = False
    for i in range(1, n // 2 + 1):
        if n % i != 0:
            continue
        pre = s[:i]
        suff = s[-i:]
        prec = 0
        suffx = 0
        for j, ch in enumerate(s):
            if pre[j % i] != ch:
                prec += 1
            if suff[j % i] != ch:
                suffx += 1
        if suffx < 2 or prec < 2:
            print(i)
            done = True
            break
    if not done:
        print(n)
