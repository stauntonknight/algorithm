import math
primes = set()
non_primes = set()

def is_prime(n):
    if n in primes:
        return True
    if n in non_primes:
        return False
    if n < 2:
        return False
    x = int(math.sqrt(n))
    if x * x == n:
        non_primes.add(n)
        return False
    for i in range(2, x+1):
        if n % i == 0:
            non_primes.add(n)
            return False
    primes.add(n)
    return True

i = 3
while True:
    if is_prime(i):
        i = i + 2
        continue
    anomaly = True
    limit = math.sqrt(i / 2)
    for j in range(1, int(limit) + 1):
        if is_prime(i - 2 * j * j):
            print (i, j)
            anomaly = False
            break
    if anomaly:
        break
    i = i + 2
print(i)
            

    

