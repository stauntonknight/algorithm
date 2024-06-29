T = int(input())
for _ in range(T):
    n = int(input())
    s = list(input())
    on = 0
    for ch in s:
        if ch == '1':
            on += 1
    # print(s, on)
    if on & 1:
        print("NO")
        continue
    if on > 2 or on < 2:
        print("YES")
        continue
    for i, ch in enumerate(s):
        if ch == '1':
            if s[i + 1] == '1':
                print("NO")
                break
            else:
                print("YES")
                break
    

