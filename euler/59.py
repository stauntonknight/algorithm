from collections import defaultdict
import re
import string

f = open("59.in", "r")
line = f.readline()
nums = line.split(",")
numbers = []
for n in nums:
    numbers.append(int(n))
candidates = [set(), set(), set()]
printables = set(c for c in string.printable)

for index in range(0, 3):
    for i in range(ord('a'), ord('z') + 1):
        print ("Checking now %s" % chr(i))
        j = index
        poss = True
        while j < len(numbers) and poss:
            value = i ^ numbers[j]
            value = chr(value)
            if value not in printables:
                poss = False
                print("Not possible %s" % value)
            j += 3
        if poss:
            candidates[index].add(i)
print(candidates)
for char1 in candidates[0]:
    for char2 in candidates[1]:
        for char3 in candidates[2]:
            key = [char1, char2, char3]
            i = 0
            dec = ""
            for c in numbers:
                dec += str(chr(c ^ key[i%3]))
                i += 1
            print(dec)


