from collections import Counter, defaultdict
T = int(input())
for _ in range(T):
    n,m,k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    counter = Counter(sorted(B))
    i = m
    curr = Counter(sorted(A[:m]))
    match_nums = sum((curr & counter).values())
    ans = 0
    if match_nums >= k:
        ans += 1
    for i in range(m, n):
        st = i - m
        first_char = A[st]
        if curr[first_char] <= counter[first_char]:
            match_nums -= 1
        curr[first_char] -= 1
        curr_char = A[i]
        curr[curr_char] += 1
        if curr[curr_char] <= counter[curr_char]:
            match_nums += 1
        # print(i, st, curr, match_nums)
        if match_nums >= k:
            ans += 1
    print(ans)

         



        
