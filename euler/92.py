from enum import Enum
class State(Enum):
    ONE = 1
    EIGHTY_NINE = 2
    UNKNOWN = 3

num = 10000001
dp = [State.UNKNOWN] * num
dp[1] = State.ONE
dp[89] = State.EIGHTY_NINE

def fill(curr):
    if dp[curr] != State.UNKNOWN:
        return dp[curr]
    total_sum = 0
    orig = curr
    while curr:
        x = curr%10
        total_sum, curr = total_sum + x * x, curr // 10
    if dp[total_sum] != State.UNKNOWN:
        val = dp[total_sum]
    else:
        val = fill(total_sum)
    dp[orig] = val
    return dp[orig]
    
kount = 0
for i in range(1, num):
    x = fill(i)
    if (x == State.EIGHTY_NINE):
        kount = kount + 1
    else:
        print(i)
print(kount)


