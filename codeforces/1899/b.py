import math
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split(' ')))
    def get(k):
        minim = float('inf')
        maxim = float('-inf')
        for i in range(N // k):
            curr = 0
            for j in range(k):
                curr = curr + arr[i * k + j]
            maxim = max(maxim, curr)
            minim = min(minim, curr)
        return maxim - minim
    
    best = max(arr) - min(arr)
    for i in range(2, (int)(math.sqrt(N)) + 1):
        if N % i == 0:
            best = max(best, get(i), get(N // i))
    print(best)
            
            
    