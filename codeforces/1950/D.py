from functools import cache
T = int(input())
def test(x):
    return set(str(x)) - set("01")
ans = []
@cache
def poss(n):
    if test(n):
        return True
    for each in ans:
        if n % each == 0 and poss(n // each):
            return True
    return False
l = 6
curr = 0

last = [1]
done = False
for i in range(l):
    if done:
        break
    news = []
    for j in last:
        curr = j * 10
        curr1 = j * 10 + 1
        news.append(curr)
        news.append(curr1)
        ans.append(curr)
        ans.append(curr1)
    last = news
for _ in range(T):
    N = int(input())
    if poss(N):
        print("YES")
    else:
        print("NO")
        
            
