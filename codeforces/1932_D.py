T = int(input())
def comp(x, y, trump):
    if len(x) != 2 or len(y) != 2:
        raise 'Error'
    if x[1] == trump and y[1] != trump:
        return True
    if x[1] != trump and y[1] == trump:
        return False
    return int(x[0]) > int(y[0])

for _ in range(T):
    N = int(input())
    trump = input()
    cards = input().split()
    def get(x):
        ans = 0
        if x[1] == trump:
            ans = 100
        return ans + int(x[0])
    cards = sorted(cards, key=get)
    print(cards)
    assert(len(cards) == 2 * N)
    print(cards)