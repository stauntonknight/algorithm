pentas = []
a = set()

def is_penta(x):
    target = x * 2
    i = 1
    while True:
        t = i * (3 * i - 1)
        if t == target:
            return True
        if (t > target):
            return False
        i = i + 1

t = 1
min_diff = 100000000
first = -1
last = -1
while True:
    penta = t * (3 * t - 1)
    penta = penta / 2
    for i in pentas:
        if (penta - i) in a and is_penta(penta + i):
            diff = penta - i
            if diff < min_diff or a == -1:
                min_diff = diff
                first = i
                last = penta
                print (first)
                print (last)
                print(last - first)
    a.add(penta)
    pentas.extend([penta])

    t = t + 1

