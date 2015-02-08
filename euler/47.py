import math;

search = True
minim = 2 * 3 * 5 * 7
num = 4

prime_cache = {}

def prime(n):
    if n in prime_cache:
        return prime_cache.get(n)
    prime_cache[n] = False
    k = math.floor(math.sqrt(n))
    for i in range(2, k + 1):
        if n % i == 0:
            return False
    prime_cache[n] = True
    return True

num_fact_cache = {}
def num_fact(n):
    if n in num_fact_cache:
        return num_fact_cache[n]
    count = 0
    for i in range (2, math.floor(n + 1)):
        if n % i == 0:
            k = n
            while k % i == 0:
                k = k / i
            count = 1 + num_fact(k)
            break
    num_fact_cache[n] = count
    return count
 
while True:
    print("Checking %d" % minim)
    a = num_fact(minim) == num
    b = num_fact(minim+1) == num
    c = num_fact(minim+2) == num
    d = num_fact(minim+3) == num
    if a and b and c and d:
        print("%d" % minim)
        break
    t = 0
    if not a:
        t = minim + 1
    if not b:
        t = minim + 2
    if not c:
        t = minim + 3
    if not d:
        t = minim + 4
    minim = t
