import sys

# f = open("82_example.txt", "r")
f = open("p082_matrix.txt", "r")

array = [[int(t) for t in x.split(",")] for x in f]

max_row = len(array)
max_col = len(array[0])

# Solution 1
def is_valid(x, y, dx, dy):
    if x + dx < 0 or x + dx >= max_row:
        return False
    if y + dy < 0 or y + dy >= max_col:
        return False
    return True

dp = []
for i in range(0, max_row):
    a = []
    for j in range(0, max_col):
        k = sys.maxsize
        a.append(k)
    dp.append(a)
for i in range(0, max_row):
    dp[i][max_col-1] = array[i][max_col-1]

for j in reversed(range(max_col)):
    for i in range(max_row):
        if is_valid(i, j , -1, 0):
            dp[i][j] = min(dp[i][j], dp[i-1][j] + array[i][j])
        if is_valid(i, j , 0, 1):
            dp[i][j] = min(dp[i][j], dp[i][j+1] + array[i][j])
    for i in reversed(range(max_row)):
        if is_valid(i, j , 1, 0):
            dp[i][j] = min(dp[i][j], dp[i+1][j] + array[i][j])
        if is_valid(i, j , 0, 1):
            dp[i][j] = min(dp[i][j], dp[i][j+1] + array[i][j])

ans = sys.maxsize

for i in range(max_row):
    ans = min(ans, dp[i][0])
print(ans)

# Solution 2.


dp1 = []
for i in range(0, max_row):
    dp1.append(0)
for i in range(0, max_row):
    dp1[i] = array[i][max_col-1]
for j in range(max_col - 1):
    dp1[0] += array[0][j]
    for i in range(1, max_row):
        dp1[i] = min(dp1[i - 1] + array[i][j], dp1[i] + array[i][j])
    for i in reversed(range(max_row - 1)):
        dp1[i] = min(dp1[i+1] + array[i][j], dp1[i])

for i in range(max_row):
    ans = min(ans, dp1[i])
print(ans)

