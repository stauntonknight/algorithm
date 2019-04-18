import sys

f = open("83_example.txt", "r")
f = open("p083_matrix.txt", "r")

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
dp[max_row-1][max_col-1] = array[i][max_col-1]


prev_ans = sys.maxsize
ans = -1

while ans != prev_ans:
    prev_ans = ans
    for j in reversed(range(max_col)):
        for i in reversed(range(max_row)):
            if is_valid(i, j , -1, 0):
                dp[i][j] = min(dp[i][j], dp[i-1][j] + array[i][j])
            if is_valid(i, j , 0, 1):
                dp[i][j] = min(dp[i][j], dp[i][j+1] + array[i][j])
            if is_valid(i, j , 1, 0):
                dp[i][j] = min(dp[i][j], dp[i+1][j] + array[i][j])
            if is_valid(i, j , 0, -1):
                dp[i][j] = min(dp[i][j], dp[i][j-1] + array[i][j])
    ans = dp[0][0]

print(ans)


