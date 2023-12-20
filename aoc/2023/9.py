
with open("9.in") as f:
    l = f.readlines()
    total = 0
    for line in l:
        line = line.strip();
        line_int = list(map(lambda x: int(x), line.split()))
        last = line_int[0]
        val = sum(line_int) == 0
        curr = -1
        while not val:
            l1 = [i - j for i, j in zip(line_int[1:], line_int[:-1])]
            if not l1:
                val = True
                continue
            val = True
            for x in l1:
                if x != 0:
                    val = False
                    break
            line_int = l1
            last = last + curr * l1[0]
            curr = curr * - 1
        total = total + last
    print(total)



