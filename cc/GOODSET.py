#/usr/bin/python


T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    a = 1
    b = 2
    if n >= 1:
        print(a, end = " ")
        n = n - 1
    if n >= 1:
        print(b, end = " ")
        n = n - 1
    while n > 0:
        n = n - 1
        x = a + b + 1
        a = b
        b = x
        print(x, end = " ")
    print()

        

