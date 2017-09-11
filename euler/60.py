TARGET = 5
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    
def is_compat(i, j):
    a = str(i) + str(j)
    b = str(j) + str(i)
    val = is_prime(int(a)) and is_prime(int(b))
    return val

N = 10000

primes = [True] * N;
count = 0
primes [0] = False
primes[1] = False
i = 2
while i < N:
    if primes[i]:
        j = i * i
        while j < N:
            primes[j] = False
            j += i
    i = i + 1
primes_all = [i for i in range(len(primes)) if primes[i] is True]

print("Forming compatibility")

compatibility = {}
for i in range(len(primes_all)):
    for j in range(i + 1, len(primes_all)):
        num1 = primes_all[i]
        num2 = primes_all[j]
        if is_compat(num1, num2):
            if not num1 in compatibility:
                compatibility[num1] = []
            compatibility[num1].append(num2)

            if not num2 in compatibility:
                compatibility[num2] = []
            compatibility[num2].append(num1)

print("Formed compatibility")
for k in compatibility:
    compatibility[k] = set(compatibility[k])

print(compatibility[13].intersection(compatibility[6733]).intersection(compatibility[5701]).intersection(compatibility[5197]))

all_2 = {}

for k,v in compatibility.items():
    for k1, v1 in compatibility.items():
        if k != k1 and k in compatibility[k1]:
            v2 = v.intersection(v1)
            if len(v2) >= TARGET - 2:
                all_2[(k,k1)] = v2

count = len(all_2)
min_val = 100000
array = []

for k, v in all_2.items():
    count -= 1
    print(count)
    for k1, v1 in all_2.items():
        x = [k[0], k[1], k1[0], k1[1]]
        is_valid = True
        if len(set(x)) != 4:
            continue
        for t in range(0, len(x)):
            for j in range(t + 1, len(x)):
                if x[j] not in compatibility[x[t]]:
                    is_valid = False
        if is_valid :
            left = v.intersection(v1)
            if len(left) >= TARGET - 4:
                val = sum(x)
                if min_val > val:
                    min_val = val
                    array = x
print(min_val, array)
