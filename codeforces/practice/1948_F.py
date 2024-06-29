s = input()
n, q  = list(map(int, s.split()))
gold = list(map(int, input().split()))
silver = list(map(int, input().split()))
queries = []
for j in range(q):
    queries.append(list(map(int, input().split())))
mod = 998244353

