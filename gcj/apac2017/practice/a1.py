from sets import Set
t = raw_input()
for x in range(0,int(t)):
    ans = 1
    print "Case #%d:" % (x+1),
    s = raw_input()
    for a in range(len(s)):
        chars = Set()
        if a > 0:
            chars.add(s[a-1])
        if a < len(s) - 1:
            chars.add(s[a+1])
        chars.add(s[a])
        ans = (ans * len(chars)) % 1000000007

    print ans
    

