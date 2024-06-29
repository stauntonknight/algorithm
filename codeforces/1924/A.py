T = int(input())
for _ in range(T):
    n,k,_ = list(map(int, input().split()))
    s = input()
    distinct = set()
    knt = 0
    last_chars = []
    for ch in s:
        distinct.add(ch)
        if len(distinct) == k:
            knt += 1
            last_chars.append(ch)
            distinct = set()
    if knt >= n:
        print("YES")
    else:
        print("NO")
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch not in distinct:
                print(''.join(last_chars + [ch] * (-len(last_chars) + n)))
                break


