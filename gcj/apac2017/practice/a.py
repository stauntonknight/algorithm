t = raw_input()
for x in range(0,int(t)):
    print "Case #%d:" % (x+1),
    s = raw_input()
    dp = [0 for a in range(len(s) + 1)]
    dp[len(s) - 1] = 1
    if s[len(s) - 1] != s[len(s) - 2]:
        dp[len(s) - 1] += 1
    for j in range(len(s) - 2, -1, -1):
        if s[j] != s[j+1]:
            dp[j] += dp[j+1]
        if j != 0 and s[j] != s[j-1]:
            dp[j] += dp[j+1]
        dp[j] += dp[j+1]
    print dp[0]
