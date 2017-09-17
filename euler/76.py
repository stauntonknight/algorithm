a = {}

def num_ways(n, max):
    if n in a and max in a[n]:
        return a[n][max]
    if n not in a:
        a[n] = {}
    if n == 0:
        return 1
    i = 1
    total = 0
    while i <= max and i <= n:
        total += num_ways(n - i, i)
        i += 1
    a[n][max] = total
    return total


print(num_ways(100, 99))
