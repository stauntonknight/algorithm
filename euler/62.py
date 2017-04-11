i = 1
d = dict()
min = dict()
while True:
    n = ''.join(sorted(str(i * i * i)))
    if n in d:
        d[n] = d[n] + 1
    else:
        d[n] = 1
    if d[n] == 5:
        print(min[n])
        break
    if n not in min:
        min[n] = i * i * i
    i += 1
