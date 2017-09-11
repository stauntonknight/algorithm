limit = 10000

primes = primelist(limit)

s1 = dict()
s2 = set()
s3 = set()
s4 = set()

for p in primes:
    s1[p] = set()
    
    for s in s1:
        if isprime(int(str(p) + str(s)), primes) and isprime(int(str(s) + str(p)), primes):
            s1[s].add(p)
            s1[p].add(s)
            s2.add((s, p))
            
    for s in s2:
        if p in s1[s[0]] and p in s1[s[1]]: s3.add((s[0], s[1], p))
    for s in s3:
        if p in s1[s[0]] and p in s1[s[1]] and p in s1[s[2]]: s4.add((s[0], s[1], s[2], p))
    for s in s4:
        if p in s1[s[0]] and p in s1[s[1]] and p in s1[s[2]] and p in s1[s[3]]: print p, s
