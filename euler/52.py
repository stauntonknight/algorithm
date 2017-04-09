
def is_same(num):
    if (sum(map(int, str(num))) % 3 != 0):
            return False
    a = set()
    for i in range(1,6):
        val = str(num * i)
        a.add(''.join(sorted(val)))

    if (num == 142857):
        print(a)
    return len(a) == 1

for i in range(1000,10000000):
    for j in range(10, 15):
        num = int(str(j) + str(i))
        if (is_same(num)):
            print(num)
            raise "Done"



