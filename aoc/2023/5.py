from functools import cache
class RangeContainer:
    def __init__(self, input):
        destination = input[0]
        source = input[1]
        range = input[2]
        self.source = source
        self.destination = destination
        self.range = range
    
    def match(self, value):
        if value >= self.destination and value < self.destination + self.range:
            return self.source + value - self.destination
        else:
            return None

    def __str__(self):
        return f"{self.destination} {self.source} {self.range}"

with open("5a.in", "r") as f:
    content = f.read()
    lines = content.splitlines()
    seeds = []
    lists = [[] for _ in range(7)]
    names = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"] 
    names_d = {}
    for k, v in enumerate(names):
        names_d[v] = k
    i = 0
    seeds = []
    ind = -1
    for l in lines:
        if not l:
            ind = -1
            continue
        elif l.startswith('seeds:'):
            seeds = list(map(int, l.strip().split(':')[1].split()))
        elif " map:" in l:
            ind = names_d[l.split()[0]]
        else:
            lists[ind].append(RangeContainer(list(map(int, l.split()))))
    minim_l = 1e100
    val = None
    
    @cache
    def get_ans(start, index):
        if index < 0:
            return start
        l = lists[index]

        for each in l:
            new_s = each.match(start)
            if new_s != None:
                start = new_s
                break
        return get_ans(start, index - 1)
    i = 0

    def belongs(i):  
        for si in range(0, len(seeds), 2):
            s_start = seeds[si]
            s_range = seeds[si + 1]
            if i >= s_start and i < s_start + s_range:
                return True
        return False
    
    while True:
        a = get_ans(i, len(lists) - 1) 
        if belongs(a):
            print("Ans", i)
            break
        i = i + 1

