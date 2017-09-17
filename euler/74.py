def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fact(n):
    val = 1;
    while n > 1:
        val = val * n
        n -= 1
    return val

@memoize
def get_chain(n):
    seen = {}
    count = 0
    while True:
        if n in seen:
            return count
        seen[n] = True
        count += 1
        val = 0
        while n > 0:
            val += fact(n % 10)
            n //= 10
        n = val
    return count

ans = 0
for i in range(1, 1000001):
    print("NEW ONE ", i)
    len = get_chain(int(i))
    if len == 60:
        ans += 1
print(ans)
