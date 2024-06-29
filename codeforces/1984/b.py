from functools import cache
T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    while n > 0:
        arr.append(n % 10)
        n = n // 10
    l = len(arr)
    @cache
    def poss(i, carry):
        if i == l:
            return carry == 0
        if i == l - 1 and arr[i] == carry:
            return True
        for cand in range(5, 10):
            nxt = arr[i] - cand - carry
            nxt_carry = 0
            if nxt < 0:
                nxt = nxt + 10
                nxt_carry = 1
            if 5 <= nxt <= 9:
                # print(cand, nxt, nxt_carry, arr[i])
                if poss(i + 1, nxt_carry):
                    return True
        return False
    print("YES") if poss(0, 0) else print("NO")
                        