from collections import defaultdict, Counter
from functools import cmp_to_key

FIVE = 7
FOUR = 6
FH = 5
THREE = 4
TWOPAIR = 3
ONEPAIR = 2
HIGH = 1
ranks = ['J','2', '3', '4','5', '6','7','8','9','T','Q','K','A']
rm = {}
for i in range(len(ranks)):
    rm[ranks[i]] = i

def find_hand(s):
    d = defaultdict(int)
    for ch in s:
        d[ch] += 1
    tm = max(d.values())
    tm_c = Counter(d.values())
    if tm >= 4:
        return FOUR if tm == 4 else FIVE
    if len(d.values()) == 2:
        return FH
    if tm == 3:
        return THREE
    if tm_c[2] == 2:
        return TWOPAIR
    if tm_c[2] == 1:
        return ONEPAIR
    return HIGH

def compare(s1, s2):
    h1 = find_hand(s1)
    h2 = find_hand(s2)
    if h1 != h2:
        return 1 if h1 > h2 else -1
    i = 0
    while i < len(s1):
        if s1[i] != s2[i]:
            return rm[s1[i]] - rm[s2[i]]
        i = i + 1
    return 0
def compare21(s1, s2):
    h1 = find_hand(s1[0])
    h2 = find_hand(s2[0])
    if h1 != h2:
        return 1 if h1 > h2 else -1
    i = 0
    while i < len(s1[0]):
        if s1[0][i] != s2[0][i]:
            return rm[s1[0][i]] - rm[s2[0][i]]
        i = i + 1
    return None

def compare2(s1, s2):
    h1 = find_hand(s1[0])
    h2 = find_hand(s2[0])
    if h1 != h2:
        return 1 if h1 > h2 else -1
    i = 0
    while i < len(s1[0]):
        if s1[1][i] != s2[1][i]:
            return rm[s1[1][i]] - rm[s2[1][i]]
        i = i + 1

def best_hand(s):
    d = defaultdict(int)
    for ch in s:
        d[ch] += 1
    all = set()
    for ch in s:
        if ch != 'J':
            all.add(ch)
    jcount = d['J']
    poss = [(s,s)]
    def fill(pref, n, st):
        if n == 0:
            return [''.join(pref)]
        ans = []
        for ch in st:
            ans.extend(fill(pref + [ch], n - 1, st))
        return ans
    variants = []
    if jcount != 0:
        variants.extend(fill([''], jcount, all | set(['A'])))
    
    for variant in variants: 
        i = 0
        vi = 0
        curr = []
        while i < len(s):
            if s[i] == 'J':
                curr.append(variant[vi])
                vi += 1
            else:
                curr.append(s[i])
            i = i + 1
        poss.append((''.join(curr), s))
    poss = sorted(poss, key=cmp_to_key(compare21))
    return poss[-1]

with open("7.in") as input:
    lines = input.readlines()
    bid = {}
    for l in lines:
        l = l.strip().split()
        bid[l[0]] = int(l[1])
    hands = list(bid.keys())
    th = []
    mth = {}
    for h in hands:
        xx = best_hand(h)[0]
        mth[xx] = h
        th.append((xx, h))
    
    sh = sorted(th, key=cmp_to_key(compare2))
    ans = 0
    for i, each in enumerate(sh):
        ans = ans + (i + 1) * bid[each[1]]
    print(ans)
    
