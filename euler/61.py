MAX = 10000
MIN = 1000

import itertools

tri = {}

n = 1
while True:
    val = n * (n + 1)
    val /= 2
    n += 1
    if val >= MAX:
        break
    if val < MIN:
        continue
    key = val / 100
    key = int(key)
    val = int(val)
    if key not in tri:
        tri[key] = []
    tri[key].append(val)

square = {}

n = 1
while True:
    val = n * n
    n += 1
    if val >= MAX:
        break
    if val < MIN:
        continue
    key = val / 100
    key = int(key)
    val = int(val)
    if key not in square:
        square[key] = []
    square[key].append(val)

penta = {}

n = 1
while True:
    val = n * (3 * n - 1)
    val /= 2
    n += 1
    if val >= MAX:
        break
    if val < MIN:
        continue
    key = val / 100
    key = int(key)
    val = int(val)
    if key not in penta:
        penta[key] = []
    penta[key].append(val)


hexa = {}

n = 1
while True:
    val = n * (2 * n - 1)
    n += 1
    if val >= MAX:
        break
    if val < MIN:
        continue
    key = val / 100
    key = int(key)
    val = int(val)
    if key not in hexa:
        hexa[key] = []
    hexa[key].append(val)

hepta = {}

n = 1
while True:
    val = n * (5 * n - 3)
    val /= 2
    n += 1
    if val >= MAX:
        break
    if val < MIN:
        continue
    key = val / 100
    key = int(key)
    val = int(val)
    if key not in hepta:
        hepta[key] = []
    hepta[key].append(val)


octa = {}

n = 1
while True:
    val = n * (3 * n - 2)
    n += 1
    if val >= MAX:
        break
    if val < MIN:
        continue
    key = val / 100
    key = int(key)
    val = int(val)
    if key not in octa:
        octa[key] = []
    octa[key].append(val)

inputs = [ tri, square, penta, hexa, hepta, octa]
array = range(6)
for combination in itertools.permutations(array):
    print(combination)
    for _, v in inputs[combination[0]].items():
        for j in v:
            j1 = int(j % 100)
            if not j1 in inputs[combination[1]]:
                continue
            for k in inputs[combination[1]][j1]:
                k1 = int(k % 100)
                if not k1 in inputs[combination[2]]:
                    continue
                for l in inputs[combination[2]][k1]:
                    l1 = int(l % 100)
                    if not l1 in inputs[combination[3]]:
                        continue
                    for m in inputs[combination[3]][l1]:
                        m1 = int(m % 100)
                        if not m1 in inputs[combination[4]]:
                            continue
                        for n in inputs[combination[4]][m1]:
                            n1 = int(n % 100)
                            if not n1 in inputs[combination[5]]:
                                continue
                            for o in inputs[combination[5]][n1]:
                                t1 = int(o % 100)
                                t2 = int(j / 100)
                                print ("Checking", t1, t2)
                                print ("Checking", j,k,l,m,n,o)
                                if t1 == t2:
                                    print("ANSWER")
                                    print(j+k+l+m+n+o)
