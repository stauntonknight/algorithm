from functools import cache

T = int(input())

mx = float('-inf')
for _ in range(T):
    s = input()
    n, x = list(map(int, s.split()))
    a = list(map(int, input().split()))
    @cache
    def get(i, curr, prev):
        if prev > x:
            return mx
        # print(i, curr, prev)
        if i == len(a):
            if (curr | prev) <= x:
                return 0
            return mx
        ans = get(i + 1, curr ^ a[i], prev)
        # print(i, curr, prev, ans)
        ans = max(ans, 1 + get(i + 1, a[i], curr | prev))
        # print(i, curr, prev, ans)
        return ans
    val = get(0, 0, 0)
    if val == mx:
        print("-1")
    else:
        print(val)

