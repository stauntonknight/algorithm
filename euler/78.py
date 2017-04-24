a = dict()
n = 0
a[0] = 1
while True:
    n += 1
    sum = 0
    gen_f = 1
    sign = 1
    found = False
    while True:
        p1 = int(gen_f * (gen_f * 3 + 1) / 2)
        p2 = int(-gen_f * (-gen_f * 3 + 1) / 2)
        if p1 <= n:
            sum = sum + a[n - p1] * sign
        if p2 <= n:
            sum = sum + a[n - p2] * sign
        sum = sum % 1000000
        gen_f += 1
        sign = sign * -1
        if p2 > n and p1 > n:
            a[n] = sum
            if sum % 1000000 == 0:
                print(sum)
                print(n)
                found = True
            break
    if found:
        break

