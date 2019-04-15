cache = {}
def get_num(odd, even):
    if odd == 0:
        return "Even"
    if not odd in cache:
        cache[odd] = {}
    if even in cache[odd]:
        return cache[odd][even]
    if even == 0:
        if odd == 1:
            return "Odd"
        num_even = int(odd / 2)
        num_odd = odd - 2*num_even
        cache[odd][even] = get_num(num_odd, num_even)
        return cache[odd][even]
    minim = min(odd, even)
    cache[odd][even] = get_num(odd, even - minim)
    return cache[odd][even]

T = int(input())
i = 1
while i <= T:
    i += 1
    n1, n2 = map(int, input().split())
    odd = int((n2 - n1 + 1) / 2)
    even = odd
    if n1 & 1 and n2 & 1:
        odd += 1
    if not (n1 & 1) and not (n2 & 1):
        even += 1
    print(get_num(odd, even))

