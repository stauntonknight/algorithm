import math

def is_triangle(n):
    target = n * 2
    v = int(math.sqrt(target))
    return v * (v + 1) == target

with open('42.in', 'r') as f:
    total = 0
    for line in f:
        sum = 0
        line = line[:-1]
        for c in line:
            sum = sum + ord(c) - ord('A') + 1
        if is_triangle(sum):
            total += 1
print(total)

