import sys

T = int(input())

i = 1
while i <= T:
    i += 1
    s1 = input()
    s2 = input()
    j = 0
    poss = False
    while j < 8:
        k = 0
        now = ""
        while k < 3:
            ch = ''
            if 1 << k & j:
                ch = s1[k]
            else:
                ch = s2[k]
            k += 1
            now += ch
        j += 1
        if ''.join(sorted(now)) == "bbo":
            poss = True
            break
    if poss:
        print("yes")
    else:
        print("no")
