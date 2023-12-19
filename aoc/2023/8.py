from math import gcd
from functools import reduce

with open("8.in") as input:
    lines = input.readlines()
    dir = lines[0].strip()
    
    map = {}
    for l in lines[1:]:
        l = l.strip()
        if not l:
            continue
        x,_,y,z = l.split()
        map[x] = (y[1:-1], z[:-1])
    curr = []
    for x in map.keys():
        if x[-1] == 'A':
            curr.append(x)
    kount = 0
    i = 0
    seen = {}
    def get_next(x, ch):
        if ch == 'L':
            return map[x][0]
        else:
            return map[x][1]
    cycle = [-1] * len(curr)
    kount = 0
    for i, c in enumerate(curr):
        while True:
            if i not in seen:
                seen[i] = {}
            if c not in seen[i] or c[-1] != 'Z':
                seen[i][c] = kount
            else:
                cycle[i] = kount - seen[i][c]
                break
            c = get_next(c, dir[kount % len(dir)])
            kount = kount + 1
    def lcm(arr):
        return reduce(lambda x, y: x* y // gcd(x, y), arr)
    print(lcm(cycle))
    
        

        