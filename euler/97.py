# Find all 6 digit remainders
a = [1]
j = 0
while True:
    a.append(2 * a[j])
    j += 1
a = [x % 1000000 for x in a]

